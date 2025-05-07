import csv
from collections import namedtuple

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    headers = next(reader)
    Row = namedtuple("Row", headers)
    for r in reader:
        row = Row(*r)
        print(row)
