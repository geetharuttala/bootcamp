def compose(f, g):
    return lambda x: f(g(x))

add1 = lambda x: x + 1
double = lambda x: x * 2

composed = compose(double, add1)
print(composed(3))