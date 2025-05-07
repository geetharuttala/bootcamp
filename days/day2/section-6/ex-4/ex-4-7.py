import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def do_something():
    logger.info("Doing something...")

do_something()

# __name__ helps organize logs per module in larger apps.
