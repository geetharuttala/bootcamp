import sys

gen = (x for x in range(1000000))
lst = [x for x in range(1000000)]

print(f"Generator size: {sys.getsizeof(gen)} bytes")
print(f"List size: {sys.getsizeof(lst)} bytes")
