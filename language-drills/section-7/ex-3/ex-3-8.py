import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def risky_op():
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        logger.error("Critical failure occurred", exc_info=True)
        raise

try:
    risky_op()
except Exception:
    print("Handled at top level")
