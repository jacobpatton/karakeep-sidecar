import os
import logging
import asyncio
import json
from fastapi import FastAPI, BackgroundTasks, Header, HTTPException, Request, Response
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict
import httpx
import aiosqlite

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("karakeep-sidecar")

app = FastAPI()

# Environment Variables
KARAKEEP_URL = os.getenv("KARAKEEP_URL", "http://web:3000") 
KARAKEEP_API_KEY = os.getenv("KARAKEEP_API_KEY")
SIDECAR_API_KEY = os.getenv("SIDECAR_API_KEY") 
SIDECAR_API_KEY = os.getenv("SIDECAR_API_KEY") 
DB_PATH = "data/queue.db"
os.makedirs("data", exist_ok=True)

if not KARAKEEP_API_KEY:
    logger.warning("KARAKEEP_API_KEY is not set. Forwarding will fail.")

# Reuse client
client = httpx.AsyncClient(timeout=30.0)

# Request Model
class Tag(BaseModel):
    id: Optional[str] = None
    name: str

class BookmarkRequest(BaseModel):
    url: str
    title: Optional[str] = None
    note: Optional[str] = None
    tags: Optional[List[Tag | str]] = None 
    archived: Optional[bool] = False
    favourited: Optional[bool] = False
    listId: Optional[str] = None
    type: str = "link" 
    
    class Config:
        extra = "allow" 

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS queue (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                payload TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                attempts INTEGER DEFAULT 0,
                status TEXT DEFAULT 'pending'
            )
        """)
        await db.commit()

async def forward_to_karakeep(payload: Dict[str, Any]) -> bool:
    target_url = f"{KARAKEEP_URL}/api/v1/bookmarks"
    headers = {
        "Authorization": f"Bearer {KARAKEEP_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        logger.info(f"Forwarding URL: {payload.get('url')} to {target_url}")
        response = await client.post(target_url, json=payload, headers=headers)
        
        if response.status_code in (200, 201):
            logger.info("Successfully forwarded bookmark.")
            return True
        elif response.status_code == 409: # Conflict / Already exists
             logger.info("Bookmark already exists (409). Marking as success.")
             return True
        else:
            logger.error(f"Failed to forward: {response.status_code} - {response.text}")
            return False
            
    except httpx.RequestError as exc:
        logger.error(f"Network error: {exc}")
        return False
    except Exception as e:
        logger.exception(f"Unexpected error in forwarder: {e}")
        return False

async def process_queue():
    logger.info("Starting queue processor...")
    while True:
        try:
            async with aiosqlite.connect(DB_PATH) as db:
                db.row_factory = aiosqlite.Row
                # Get oldest pending item
                async with db.execute("SELECT * FROM queue WHERE status = 'pending' ORDER BY created_at ASC LIMIT 1") as cursor:
                    row = await cursor.fetchone()
                
                if row:
                    item_id = row['id']
                    payload = json.loads(row['payload'])
                    attempts = row['attempts']
                    
                    # Backoff logic
                    success = await forward_to_karakeep(payload)
                    
                    if success:
                        await db.execute("DELETE FROM queue WHERE id = ?", (item_id,))
                        await db.commit()
                        logger.info(f"Item {item_id} processed and removed from queue.")
                    else:
                        # Increment attempts
                        await db.execute("UPDATE queue SET attempts = attempts + 1 WHERE id = ?", (item_id,))
                        await db.commit()
                        logger.warning(f"Item {item_id} failed. Retrying in 10 seconds...")
                        await asyncio.sleep(10) # Wait before next attempt
                else:
                    # Queue empty
                    await asyncio.sleep(1)
                    
        except Exception as e:
            logger.error(f"Queue processor crashed: {e}")
            await asyncio.sleep(5)

@app.on_event("startup")
async def startup_event():
    await init_db()
    asyncio.create_task(process_queue())

@app.post("/api/v1/bookmarks", status_code=202)
async def create_bookmark(
    request: BookmarkRequest, 
    authorization: Optional[str] = Header(None)
):
    # 1. AUTHENTICATION
    incoming_token = None
    if authorization:
        parts = authorization.split(" ")
        if len(parts) == 2 and parts[0].lower() == "bearer":
            incoming_token = parts[1]
    
    required_key = SIDECAR_API_KEY or KARAKEEP_API_KEY
    if required_key and incoming_token != required_key:
         raise HTTPException(status_code=401, detail="Unauthorized")

    # 2. ENQUEUE TO SQLITE
    try:
        payload = request.model_dump(exclude_none=True)
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT INTO queue (payload) VALUES (?)", 
                (json.dumps(payload),)
            )
            await db.commit()
            
    except Exception as e:
        logger.error(f"Failed to write to DB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    # 3. RETURN
    return {"status": "queued", "message": "Bookmark saved to persistent queue"}

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"])
async def proxy_request(request: Request, path: str):
    """
    Catch-all proxy for everything else (Auth, other APIs).
    """
    target_url = f"{KARAKEEP_URL}/{path}"
    if request.url.query:
        target_url += f"?{request.url.query}"
        
    logger.info(f"Proxying {request.method} {path} to {target_url}")
    
    # Exclude host header to avoid confusion at target
    headers = dict(request.headers)
    headers.pop("host", None)
    headers.pop("content-length", None) # Let httpx handle this
    
    try:
        content = await request.body()
        
        req = client.build_request(
            request.method,
            target_url,
            headers=headers,
            content=content
        )
        
        response = await client.send(req, stream=True)
        
        return Response(
            content=response.read(),
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.headers.get("content-type")
        )
            
    except Exception as e:
        logger.error(f"Proxy failed: {e}")
        raise HTTPException(status_code=502, detail="Bad Gateway")

@app.on_event("shutdown")
async def shutdown_event():
    await client.aclose()
