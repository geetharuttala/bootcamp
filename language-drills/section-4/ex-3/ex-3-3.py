from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greets a person."""
    return f"Hello, {name}"

print(greet("Geetha"))
print(greet.__name__)
print(greet.__doc__)
