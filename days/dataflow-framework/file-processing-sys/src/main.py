# main.py

import threading
import time
from utils.metrics import metrics_store
from utils.tracing import trace_store
from dashboard.server import start_dashboard
from file_watcher import start_watcher

def main():
    # Start the FastAPI dashboard
    dashboard_thread = threading.Thread(
        target=start_dashboard,
        args=(metrics_store, trace_store),
        daemon=True
    )
    dashboard_thread.start()

    # Start the file watcher
    start_watcher()

    print("[MAIN] Watching folder and running dashboard. Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[MAIN] Shutting down...")

if __name__ == "__main__":
    main()
