# Updated main.py with support for state-based routing

import threading
import time
from app.utils.metrics import metrics_store
from app.utils.tracing import trace_store
from app.dashboard.server import start_dashboard
from app.file_watcher import start_watcher
from app.engine.runner import process_file


def start_dashboard_in_thread():
    """Start the FastAPI dashboard in a separate thread."""
    dashboard_thread = threading.Thread(
        target=start_dashboard,
        args=(metrics_store, trace_store),
        daemon=True
    )
    dashboard_thread.start()
    # Give the dashboard time to start up
    time.sleep(1)
    return dashboard_thread


def run_once(input_path: str, config_path: str, trace: bool = False):
    """Process a single file through the pipeline."""
    print(f"[MAIN] Running in single-file mode: {input_path}")
    # Clear any previous data to avoid duplicates when rerunning
    trace_store.clear_traces()
    metrics_store.clear_errors()

    dashboard_thread = start_dashboard_in_thread()
    process_file(input_path, config_path, trace)
    print("[MAIN] Processing complete.")

    # Keep dashboard running briefly to allow viewing results
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[MAIN] Shutting down...")


def run_watch(config_path: str):
    """Watch a folder for new files and process them."""
    print("[MAIN] Running in folder watch mode.")
    # Clear any previous data to avoid duplicates when restarting
    trace_store.clear_traces()
    metrics_store.clear_errors()

    dashboard_thread = start_dashboard_in_thread()
    watcher_thread = start_watcher(config_path)
    print("[MAIN] Watching folder... Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[MAIN] Shutting down...")