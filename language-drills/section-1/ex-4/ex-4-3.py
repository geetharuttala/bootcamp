def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment

inc = counter()
print(inc())
print(inc())
