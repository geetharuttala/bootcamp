def make_multiplier(factor):
    return lambda x: x * factor

triple = make_multiplier(3)
print(triple(10))
