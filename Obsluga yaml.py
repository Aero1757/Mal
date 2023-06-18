import yaml

# Zapis danych do pliku YAML
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
with open("data.yaml", "w") as file:
    yaml.dump(data, file)

# Odczyt danych z pliku YAML
with open("data.yaml", "r") as file:
    data = yaml.load(file, Loader=yaml.Loader)
    print(data)