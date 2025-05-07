from itertools import cycle

colors = cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors))
