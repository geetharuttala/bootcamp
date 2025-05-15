import time

start = time.time()
sum(range(1000000))
end = time.time()

print("Time taken:", end - start)
