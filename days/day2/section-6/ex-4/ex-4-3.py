import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class User:
    def __init__(self, name):
        self.name = name

user = User("Geetha")
logger.debug(f"Processing user: {user.name}")
