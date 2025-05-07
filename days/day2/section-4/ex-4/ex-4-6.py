from itertools import tee

nums = iter(range(5))
a, b = tee(nums)
print("First copy:", list(a))
print("Second copy:", list(b))
