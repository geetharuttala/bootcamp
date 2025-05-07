metrics = {
    "calls": 0,
    "errors": 0,
    "total_time": 0.0
}

def monitored_function():
    import time
    metrics["calls"] += 1
    start = time.time()
    time.sleep(0.1)
    metrics["total_time"] += time.time() - start

monitored_function()
monitored_function()
print(metrics)
