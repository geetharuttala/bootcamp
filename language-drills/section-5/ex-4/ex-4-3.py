import csv

with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
