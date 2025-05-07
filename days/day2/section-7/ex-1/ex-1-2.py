import timeit

list_time = timeit.timeit("[x*x for x in range(1000000)]", number=10)
gen_time = timeit.timeit("(x*x for x in range(1000000))", number=10)

print("List comprehension:", list_time)
print("Generator expression:", gen_time)
