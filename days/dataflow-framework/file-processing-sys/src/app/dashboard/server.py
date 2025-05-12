# Fixed version of app/dashboard/server.py

import time
from fastapi import FastAPI, status, Response
from uvicorn import Config, Server
from pathlib import Path
import asyncio
import nest_asyncio

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

WATCH_DIR = Path("watch_dir")

# Delayed import to avoid circular reference
current_file = None
processed_files = []
try:
    from app.file_watcher import current_file, processed_files
except ImportError:
    print("[DASHBOARD] file_watcher.py not yet initialized, skipping file info.")


def start_dashboard(metrics_store, trace_store):
    print("[DASHBOARD] Initializing FastAPI app...")
    app = FastAPI(title="File Processing Dashboard")

    @app.get("/")
    def home():
        return {
            "message": "Welcome to the File Processing Dashboard",
            "endpoints": [
                {"name": "/health", "description": "Health check endpoint"},
                {"name": "/stats", "description": "Processing statistics"},
                {"name": "/trace", "description": "Execution traces"},
                {"name": "/errors", "description": "Processing errors"},
                {"name": "/files", "description": "File processing status"}
            ]
        }

    @app.get("/health")
    def health():
        try:
            # Make sure the watch directories exist
            if not WATCH_DIR.exists():
                return Response(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    content="Watch directory not found"
                )
            # Use time.time() instead of asyncio.get_event_loop().time()
            return {"status": "ok", "timestamp": time.time()}
        except Exception as e:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=f"Health check failed: {str(e)}"
            )

    @app.get("/stats")
    def get_stats():
        return metrics_store.get_metrics()

    @app.get("/trace")
    def get_trace():
        traces = trace_store.get_traces()
        return {
            "count": len(traces),
            "traces": traces
        }

    @app.get("/errors")
    def get_errors():
        errors = metrics_store.get_recent_errors()
        return {
            "count": len(errors),
            "errors": errors
        }

    @app.get("/files")
    def get_files():
        try:
            # Check if directories exist before counting files
            unprocessed_count = len(list((WATCH_DIR / "unprocessed").glob("*"))) if (
                        WATCH_DIR / "unprocessed").exists() else 0
            underprocess_count = len(list((WATCH_DIR / "underprocess").glob("*"))) if (
                        WATCH_DIR / "underprocess").exists() else 0
            processed_count = len(list((WATCH_DIR / "processed").glob("*"))) if (
                        WATCH_DIR / "processed").exists() else 0

            return {
                "current": current_file,
                "recent": [
                    {"file": name, "timestamp": ts}
                    for name, ts in processed_files[-10:]
                ],
                "counts": {
                    "unprocessed": unprocessed_count,
                    "underprocess": underprocess_count,
                    "processed": processed_count,
                },
            }
        except Exception as e:
            return {
                "error": f"Failed to get file info: {str(e)}",
                "current": current_file,
                "recent": [],
                "counts": {"error": "Could not count files"}
            }

    # Try to start the server, handling potential port conflicts
    try:
        config = Config(app=app, host="0.0.0.0", port=8000, log_level="info")
        server = Server(config=config)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(server.serve())
    except OSError as e:
        if "Address already in use" in str(e):
            print("[DASHBOARD] Port 8000 already in use, trying port 8001...")
            try:
                config = Config(app=app, host="0.0.0.0", port=8001, log_level="info")
                server = Server(config=config)

                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(server.serve())
            except Exception as e2:
                print(f"[DASHBOARD] Failed to start on port 8001: {e2}")
        else:
            print(f"[DASHBOARD] Failed to start server: {e}")