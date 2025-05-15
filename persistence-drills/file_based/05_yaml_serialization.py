import yaml

class Car:
    def __init__(self, make: str, model: str, year: int, features: list[str]):
        self.make = make
        self.model = model
        self.year = year
        self.features = features

    def to_yaml(self) -> str:
        return yaml.dump(self.__dict__, sort_keys=False)

car = Car(
    make="Toyota",
    model="Camry",
    year=2022,
    features=["Bluetooth", "Backup camera", "Cruise control"]
)

car_yaml = car.to_yaml()
print("Serialized YAML:")
print(car_yaml)

# Save file
with open("car.yaml", "w") as f:
    f.write(car_yaml)