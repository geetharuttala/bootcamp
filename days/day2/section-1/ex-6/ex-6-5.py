def running_total(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total

for total in running_total([1, 2, 3]):
    print(total)
