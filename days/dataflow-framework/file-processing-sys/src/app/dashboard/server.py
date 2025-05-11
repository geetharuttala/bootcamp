# dashboard/server.py

import asyncio
from fastapi import FastAPI
from uvicorn import Config, Server
from pathlib import Path

WATCH_DIR = Path("watch_dir")

# Delayed import to avoid circular reference
current_file = None
processed_files = []
try:
    from file_watcher import current_file, processed_files
except ImportError:
    print("[DASHBOARD] file_watcher.py not yet initialized, skipping file info.")

def start_dashboard(metrics_store, trace_store):
    print("[DASHBOARD] Initializing FastAPI app...")
    app = FastAPI()

    @app.get("/")
    def home():
        return {"message": "Welcome to the File Processing Dashboard"}

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.get("/stats")
    def get_stats():
        return metrics_store.get_metrics()

    @app.get("/trace")
    def get_trace():
        return trace_store.get_traces()

    @app.get("/errors")
    def get_errors():
        return metrics_store.get_recent_errors()

    @app.get("/files")
    def get_files():
        return {
            "current": current_file,
            "recent": [
                {"file": name, "timestamp": ts}
                for name, ts in processed_files[-10:]
            ],
            "counts": {
                "unprocessed": len(list((WATCH_DIR / "unprocessed").glob("*"))),
                "underprocess": len(list((WATCH_DIR / "underprocess").glob("*"))),
                "processed": len(list((WATCH_DIR / "processed").glob("*"))),
            },
        }

    config = Config(app=app, host="0.0.0.0", port=8000, log_level="info")
    server = Server(config=config)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(server.serve())
