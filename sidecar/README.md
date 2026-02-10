# KaraKeep Sidecar

This is a lightweight FastAPI service that buffers bookmark additions for KaraKeep, preventing client-side hanging.

## Setup

1.  **Environment Variables:**
    Create a `.env` file or set these variables:
    *   `KARAKEEP_URL`: The URL of your main KaraKeep instance (e.g., `http://localhost:3000` or `http://karakeep:3000` if in the same docker network).
    *   `KARAKEEP_API_KEY`: Your KaraKeep API Key (Create one in KaraKeep Settings).
    *   `SIDECAR_API_KEY`: (Optional) If set, the extensions must use this key. If not set, they must use `KARAKEEP_API_KEY`.

2.  **Run with Docker Compose:**
    ```bash
    docker-compose -f docker-compose.sidecar.yml up -d --build
    ```

3.  **Configure Extension:**
    *   **URL:** Point your extension to `http://<your-server-ip>:8000` instead of the main KaraKeep URL.
    *   **API Key:** Use the API Key as configured.

## Development

To run locally without Docker:

```bash
cd sidecar
pip install -r requirements.txt
export KARAKEEP_API_KEY="your-key"
uvicorn main:app --reload
```
