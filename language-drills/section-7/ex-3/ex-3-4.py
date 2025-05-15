import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process(data):
    logger.debug("Entering process()")
    result = data.upper()
    logger.debug("Exiting process()")
    return result

print(process("debugging"))
