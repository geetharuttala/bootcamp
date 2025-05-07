try:
    try:
        x = int("abc")
    except ValueError:
        print("Inner: invalid int")

    y = 10 / 0
except ZeroDivisionError:
    print("Outer: division by zero")
