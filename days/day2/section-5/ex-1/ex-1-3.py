from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4, 4]
counter = Counter(nums)
print(counter.most_common(2))
