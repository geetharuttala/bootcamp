nested = [[1, 2], [3, 4]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)
