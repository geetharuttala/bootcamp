from itertools import permutations, combinations

items = [1, 2, 3]

print("Permutations of 2:")
for p in permutations(items, 2):
    print(p)

print("Combinations of 2:")
for c in combinations(items, 2):
    print(c)
