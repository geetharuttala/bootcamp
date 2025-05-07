import random
import time

data = [random.randint(0, 10000) for _ in range(10000)]

def custom_sort(arr):
    return sorted(arr)  # mimic custom sort

start = time.time()
sorted(data)
print("Built-in sort:", time.time() - start)

start = time.time()
custom_sort(data)
print("Custom sort:", time.time() - start)
