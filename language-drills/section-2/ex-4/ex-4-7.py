class DBConnection:
    def __enter__(self):
        print("Connecting to DB")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing DB connection")

with DBConnection():
    print("Running query")
