nums = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 != 0, nums))

print(doubled)
print(filtered)
