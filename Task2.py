import json

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f'Plik "{file_path}" nie istnieje.')
    except json.JSONDecodeError as e:
        print(f'Błąd dekodowania pliku JSON: {str(e)}')

def main():
    file_path = 'data.json'  # Ścieżka do pliku JSON

    # Wczytywanie pliku JSON
    json_data = load_json_file(file_path)

    if json_data:
        # Jeśli plik JSON jest poprawny, można przeprowadzić operacje na wczytanych danych
        print('Plik JSON jest poprawny.')
        print('Wczytane dane:')
        print(json_data)

if __name__ == '__main__':
    main()