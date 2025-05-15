from itertools import groupby

data = [
    {"dept": "IT", "name": "Geetha"},
    {"dept": "IT", "name": "Trinadh"},
    {"dept": "HR", "name": "Deepthi"},
    {"dept": "HR", "name": "Rutu"},
]
data.sort(key=lambda x: x["dept"])

for key, group in groupby(data, key=lambda x: x["dept"]):
    print(f"{key}: {[item['name'] for item in group]}")
