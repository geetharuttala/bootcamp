# List comprehension
evens_list = [x for x in range(10) if x % 2 == 0]
print("List:", evens_list)

# Generator
evens_gen = (x for x in range(10) if x % 2 == 0)
print("Generator:", list(evens_gen))

