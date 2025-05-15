import csv

people = [{"name": "Geetha", "age": 24}, {"name": "Dhoni", "age": 43}]

with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(people)

print("Written to output.csv")
