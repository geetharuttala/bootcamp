from concurrent.futures import ThreadPoolExecutor
import time

def work(n):
    time.sleep(0.1)
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(work, range(5)))
    print(results)
