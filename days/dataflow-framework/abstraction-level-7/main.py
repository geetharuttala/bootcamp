import threading
import time
from core.engine import ProcessingEngine
from utils.metrics import metrics_store
from utils.tracing import trace_store
from dashboard.server import start_dashboard

def main(input_file: str, config_file: str, trace: bool):
    dashboard_thread = None

    # Start the dashboard only if trace is enabled
    if trace:
        dashboard_thread = threading.Thread(
            target=start_dashboard,
            args=(metrics_store, trace_store),
            daemon=True
        )
        dashboard_thread.start()

    # Initialize and run the processing engine
    engine = ProcessingEngine(input_file, config_file, trace)
    engine.run()

    # Keep the main thread alive if tracing is enabled, so dashboard stays up
    if trace:
        print("[MAIN] Trace mode enabled. Keeping dashboard alive. Press Ctrl+C to exit.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[MAIN] Shutting down dashboard and exiting...")
