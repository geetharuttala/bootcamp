import pickle

data = {"framework": "Django", "version": 4.2}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

print("Loaded from pickle:", loaded)
