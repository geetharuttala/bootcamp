def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")  # guard against zero division
    return a / b

print(divide(10, 2))
# print(divide(5, 0))  # Uncomment to see the ValueError
