import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def greet(name):
    logger.info(f"Hello, {name}!")

greet("Geetha")
