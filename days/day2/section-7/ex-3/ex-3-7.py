def factorial(n, indent=0):
    print("  " * indent + f"factorial({n})")
    if n == 0:
        return 1
    return n * factorial(n - 1, indent + 1)

print(factorial(4))
