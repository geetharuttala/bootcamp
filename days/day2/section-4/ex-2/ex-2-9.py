def validate_args(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Only int or float allowed")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @validate_args
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))
# Uncomment to test invalid input
# print(calc.add("two", 3))
