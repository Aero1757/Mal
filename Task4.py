import yaml

def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f'Plik "{file_path}" nie istnieje.')
    except yaml.YAMLError as e:
        print(f'Błąd wczytywania pliku YAML: {str(e)}')

def main():
    file_path = 'data.yml'  # Ścieżka do pliku YAML

    # Wczytywanie pliku YAML
    yaml_data = load_yaml_file(file_path)

    if yaml_data:
        # Jeśli plik YAML jest poprawny, można przeprowadzić operacje na wczytanych danych
        print('Plik YAML jest poprawny.')
        print('Wczytane dane:')
        print(yaml_data)

if __name__ == '__main__':
    main()