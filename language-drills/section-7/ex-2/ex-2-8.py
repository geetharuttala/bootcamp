def square_gen(n):
    for i in range(n):
        yield i * i

for val in square_gen(5):
    print(val)
