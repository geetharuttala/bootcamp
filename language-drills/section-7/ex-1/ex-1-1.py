import timeit

print(timeit.timeit("sum(range(10000))", number=100))
