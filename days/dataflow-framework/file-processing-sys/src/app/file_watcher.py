# Fixed version of app/file_watcher.py

import os
import shutil
import time
from pathlib import Path
import threading
from app.engine.runner import process_file

WATCH_DIR = Path("watch_dir")
UNPROCESSED = WATCH_DIR / "unprocessed"
UNDERPROCESS = WATCH_DIR / "underprocess"
PROCESSED = WATCH_DIR / "processed"

current_file = None
processed_files = []
# Track files we've already processed to avoid duplicates
processed_filenames = set()


def recover_incomplete_files():
    """Move any files in the underprocess directory back to unprocessed"""
    for file in UNDERPROCESS.iterdir():
        if file.is_file():
            print(f"[RECOVERY] Moving {file.name} back to unprocessed/")
            shutil.move(str(file), UNPROCESSED / file.name)


def monitor_folder(config_path):
    global current_file

    while True:
        # Process only files that haven't been processed yet
        for file in sorted(UNPROCESSED.iterdir()):
            if not file.is_file():
                continue

            # Skip if we've already processed this file
            if file.name in processed_filenames:
                continue

            processing_path = UNDERPROCESS / file.name
            try:
                shutil.move(str(file), processing_path)
            except (FileNotFoundError, shutil.Error) as e:
                print(f"[WATCHER] Error moving file {file.name}: {e}")
                continue

            print(f"[WATCHER] Processing {processing_path.name}")
            current_file = processing_path.name

            try:
                process_file(processing_path, config_path)
                # Move to processed directory
                try:
                    shutil.move(str(processing_path), PROCESSED / processing_path.name)
                    # Add to processed list
                    processed_files.append((processing_path.name, time.time()))
                    processed_filenames.add(processing_path.name)
                    # Keep processed list manageable
                    if len(processed_files) > 100:
                        oldest = processed_files.pop(0)
                        # Don't remove from processed_filenames set to maintain history
                except (FileNotFoundError, shutil.Error) as e:
                    print(f"[WATCHER] Error moving processed file {processing_path.name}: {e}")
            except Exception as e:
                print(f"[ERROR] Failed to process {processing_path.name}: {e}")
                try:
                    # Move back to unprocessed directory
                    shutil.move(str(processing_path), UNPROCESSED / processing_path.name)
                except (FileNotFoundError, shutil.Error) as move_err:
                    print(f"[ERROR] Failed to move {processing_path.name} back to unprocessed: {move_err}")

            current_file = None

        # Sleep to avoid high CPU usage
        time.sleep(2)


def start_watcher(config_path):
    """Start the file watcher"""
    # Create necessary directories
    for folder in [UNPROCESSED, UNDERPROCESS, PROCESSED]:
        folder.mkdir(parents=True, exist_ok=True)

    # Recover any files that were being processed before a crash
    recover_incomplete_files()

    # Start monitoring thread
    watcher_thread = threading.Thread(target=monitor_folder, args=(config_path,), daemon=True)
    watcher_thread.start()
    return watcher_thread