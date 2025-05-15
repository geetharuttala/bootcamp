import traceback

try:
    1 / 0
except Exception:
    print("Caught an exception:")
    print(traceback.format_exc())
