import logging

debug = True

logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
logger = logging.getLogger()

logger.debug("This will show only if debug=True")
logger.info("This always shows.")
