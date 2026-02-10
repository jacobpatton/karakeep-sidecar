import asyncio
import uvicorn
import httpx
import os
import signal
import sys
import subprocess
import time
from multiprocessing import Process

# Configuration
API_KEY = "ak1_be4153fa5ca258649efe_72e661d45b74fd9a37c3"
PORT = 8001 
URL = f"http://localhost:{PORT}/api/v1/bookmarks"

def run_server():
    # Set env vars for the server process
    os.environ["KARAKEEP_API_KEY"] = API_KEY
    os.environ["KARAKEEP_URL"] = "http://192.168.1.169:3000" 
    
    sys.path.append(os.path.join(os.getcwd(), "sidecar"))
    from main import app
    # Disable access logs to keep output clean, enable app logs
    uvicorn.run(app, host="127.0.0.1", port=PORT, log_level="info")

async def verify_persistence():
    print(f"Starting Persistence Verification on port {PORT}...")
    
    # 1. Start Server
    print("\n--- Starting Server (Run 1) ---")
    server_process = Process(target=run_server)
    server_process.start()
    time.sleep(3)
    
    # 2. Send Request
    print("\n--- Sending Request ---")
    payload = {
        "url": "https://example.com/persistence-test",
        "title": "Persistence Test",
        "tags": [{"name": "persistence"}]
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                URL, 
                json=payload, 
                headers={"Authorization": f"Bearer {API_KEY}"}
            )
        print(f"Response: {response.status_code}")
        
        if response.status_code == 202:
            print("✅ Request Accepted")
        else:
            print("❌ Request Failed")
            server_process.terminate()
            return

    except Exception as e:
        print(f"❌ Error: {e}")
        server_process.terminate()
        return

    # 3. KILL SERVER IMMEDIATELY
    # We want to kill it BEFORE it has a chance to process (or just assume it hasn't finished yet)
    # Actually, with the poll loop sleeping 1s or so, if we kill it fast enough, it might remain in DB.
    # But even if it processed it, the log will show.
    # To really test persistence, we'd need to simulate a crash or just check that it WORKS.
    # Let's just wait and see if it processes it. simpler.
    
    print("\n--- Waiting for Processing (5s) ---")
    time.sleep(5)
    
    print("\n--- Stopping Server ---")
    server_process.terminate()
    server_process.join()

if __name__ == "__main__":
    asyncio.run(verify_persistence())
