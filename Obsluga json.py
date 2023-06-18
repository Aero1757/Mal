import json

# Zapis danych do pliku JSON
data = {
    "name": "Jan Kaczynski",
    "age": 30,
    "city": "Wroclaw"
}
with open("data.json", "w") as file:
    json.dump(data, file)

# Odczyt danych z pliku JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)