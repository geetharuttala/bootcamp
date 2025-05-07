class SafeBlock:
    def __enter__(self):
        print("Starting safe block")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleanup even after error!")

with SafeBlock():
    raise ValueError("Something went wrong")
