import time

def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Logger: Function started")
        result = func(*args, **kwargs)
        print("Logger: Function ended")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Timer: {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Debug: {func.__name__} called with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Debug: {func.__name__} returned {result}")
        return result
    return wrapper

@simple_logger
@timer
@debug_info
def multiply(a, b):
    return a * b

print(multiply(3, 4))
