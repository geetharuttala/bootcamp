# src/app/main.py


import threading
import time
from app.utils.metrics import metrics_store
from app.utils.tracing import trace_store
from app.dashboard.server import start_dashboard
from app.file_watcher import start_watcher
from app.engine.runner import process_file


def start_dashboard_in_thread():
   dashboard_thread = threading.Thread(
       target=start_dashboard,
       args=(metrics_store, trace_store),
       daemon=True
   )
   dashboard_thread.start()


def run_once(input_path: str, config_path: str, trace: bool = False):
   print(f"[MAIN] Running in single-file mode: {input_path}")
   start_dashboard_in_thread()
   process_file(input_path, config_path, trace)
   print("[MAIN] Processing complete.")


def run_watch(config_path: str):
   print("[MAIN] Running in folder watch mode.")
   start_dashboard_in_thread()
   start_watcher(config_path)
   print("[MAIN] Watching folder... Ctrl+C to exit.")
   try:
       while True:
           time.sleep(1)
   except KeyboardInterrupt:
       print("\n[MAIN] Shutting down...")
