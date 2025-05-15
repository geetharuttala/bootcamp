from itertools import islice

def line_gen():
    for i in range(100):
        yield f"Line {i}"

for line in islice(line_gen(), 10):
    print(line)
