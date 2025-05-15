import os
import logging

DEBUG = os.getenv("DEBUG", "False") == "True"

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)

def run():
    logging.debug("Debug info shown only if DEBUG=True")
    logging.info("Running app")

run()
