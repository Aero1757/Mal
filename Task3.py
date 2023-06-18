import json

def save_json_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'Dane zostały zapisane do pliku: {file_path}')
    except IOError:
        print(f'Wystąpił błąd podczas zapisu do pliku: {file_path}')

def main():
    # Dane do zapisania w formacie JSON
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }

    file_path = 'output.json'  # Ścieżka do pliku, gdzie mają być zapisane dane

    # Zapisywanie danych do pliku JSON
    save_json_file(data, file_path)

if __name__ == '__main__':
    main()