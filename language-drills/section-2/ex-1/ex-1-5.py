import os

filename = "test.txt"

if os.path.exists(filename):
    with open(filename) as f:
        print(f.read())
else:
    print("File does not exist (LBYL)")