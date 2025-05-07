from contextlib import suppress

with suppress(FileNotFoundError):
    with open("missing.txt") as f:
        print(f.read())
print("Program continues")
