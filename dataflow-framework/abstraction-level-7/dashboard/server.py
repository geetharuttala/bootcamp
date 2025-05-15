import asyncio
from fastapi import FastAPI
from uvicorn import Config, Server

def start_dashboard(metrics_store, trace_store):
    print("[DASHBOARD] Initializing FastAPI app...")

    app = FastAPI()

    @app.get("/stats")
    def get_stats():
        print("[DASHBOARD] /stats endpoint hit")
        return metrics_store.get_metrics()

    @app.get("/trace")
    def get_trace():
        print("[DASHBOARD] /trace endpoint hit")
        return trace_store.get_traces()

    @app.get("/errors")
    def get_errors():
        return metrics_store.get_recent_errors()

    print("[DASHBOARD] Creating Uvicorn server...")
    config = Config(app=app, host="0.0.0.0", port=8000, log_level="info")
    server = Server(config=config)

    print("[DASHBOARD] Starting server with asyncio...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(server.serve())
