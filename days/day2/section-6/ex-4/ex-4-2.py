import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
