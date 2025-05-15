import threading
import time

def greet():
    time.sleep(1)
    print("Hello from thread")

thread = threading.Thread(target=greet)
thread.start()
thread.join()
