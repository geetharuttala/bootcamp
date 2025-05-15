def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
            print("All retries failed.")
        return wrapper
    return decorator

@retry(3)
def unstable():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    print("Succeeded!")

unstable()
