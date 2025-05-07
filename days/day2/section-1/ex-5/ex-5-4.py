try:
    num = int("abc")
    result = num / 0
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
