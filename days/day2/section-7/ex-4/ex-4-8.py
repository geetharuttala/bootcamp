import logging

logging.basicConfig(level=logging.INFO)

def trace(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@trace
def add(x, y):
    return x + y

add(3, 4)
