import time
import logging

logging.basicConfig(level=logging.INFO)

def slow_function():
    start = time.time()
    time.sleep(1.2)
    duration = time.time() - start
    logging.info(f"slow_function took {duration:.2f}s")

slow_function()
