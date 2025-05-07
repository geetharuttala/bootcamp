from functools import partial

binary_converter = partial(int, base=2)
print(binary_converter("1010"))
