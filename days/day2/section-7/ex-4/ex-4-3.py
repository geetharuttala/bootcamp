import logging

logging.basicConfig(level=logging.ERROR)

def process_data(data):
    if not data:
        logging.error("[E1001] Data is empty")
        return
    print("Processing data...")

process_data("")
