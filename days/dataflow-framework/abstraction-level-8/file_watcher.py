import os
import shutil
import time
from pathlib import Path
import threading
from engine.runner import process_file

WATCH_DIR = Path("watch_dir")
UNPROCESSED = WATCH_DIR / "unprocessed"
UNDERPROCESS = WATCH_DIR / "underprocess"
PROCESSED = WATCH_DIR / "processed"

current_file = None
processed_files = []

def recover_incomplete_files():
    for file in UNDERPROCESS.iterdir():
        if file.is_file():
            print(f"[RECOVERY] Moving {file.name} back to unprocessed/")
            shutil.move(str(file), UNPROCESSED / file.name)

def monitor_folder():
    global current_file
    while True:
        for file in UNPROCESSED.iterdir():
            if not file.is_file():
                continue
            processing_path = UNDERPROCESS / file.name
            shutil.move(str(file), processing_path)
            print(f"[WATCHER] Processing {processing_path.name}")
            current_file = processing_path.name
            try:
                process_file(processing_path)
                shutil.move(str(processing_path), PROCESSED / processing_path.name)
                processed_files.append((processing_path.name, time.time()))
                if len(processed_files) > 100:
                    processed_files.pop(0)
            except Exception as e:
                print(f"[ERROR] Failed to process {processing_path.name}: {e}")
                shutil.move(str(processing_path), UNPROCESSED / processing_path.name)
            current_file = None
        time.sleep(2)

def start_watcher(config=None):
    for folder in [UNPROCESSED, UNDERPROCESS, PROCESSED]:
        folder.mkdir(parents=True, exist_ok=True)
    recover_incomplete_files()
    threading.Thread(target=monitor_folder, daemon=True).start()
