import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def do_something(user_id):
    logging.info(f"[User {user_id}] Running do_something()")

do_something("abc123")
