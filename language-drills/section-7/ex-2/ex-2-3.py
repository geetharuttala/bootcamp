import csv

def filter_csv(filepath):
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["age"]) > 30:
                yield row

# Example usage
for row in filter_csv("data.csv"):
    print(row)
    break
