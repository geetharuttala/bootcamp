from functools import lru_cache
import time

def fib_plain(n):
    if n < 2:
        return n
    return fib_plain(n-1) + fib_plain(n-2)

@lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n-1) + fib_cached(n-2)

start = time.time()
print(fib_plain(30))
print("Plain took:", time.time() - start)

start = time.time()
print(fib_cached(30))
print("Cached took:", time.time() - start)
