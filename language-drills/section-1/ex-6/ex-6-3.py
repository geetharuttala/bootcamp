it = iter([1, 2])

try:
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("Reached end of iterator")