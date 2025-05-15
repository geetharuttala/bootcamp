from itertools import count

id_gen = count(start=1)
for _ in range(5):
    print(next(id_gen))
