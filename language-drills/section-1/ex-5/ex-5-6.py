try:
    raise ValueError("Something went wrong")
except ValueError as e:
    print(f"Logging error: {e}")
    raise
