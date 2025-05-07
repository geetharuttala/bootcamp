from itertools import islice

nums = range(10)
sliced = list(islice(nums, 3, 7))
print(sliced)
