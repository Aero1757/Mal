import xml.etree.ElementTree as ET

def save_xml_file(data, file_path):
    try:
        root = ET.Element('root')
        # Tworzenie elementów XML na podstawie danych
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f'Dane zostały zapisane do pliku: {file_path}')
    except IOError:
        print(f'Wystąpił błąd podczas zapisu do pliku: {file_path}')

def main():
    # Dane do zapisania w formacie XML
    data = {
        'name': 'Jan Kaczynski',
        'age': 30,
        'city': 'Wroclaw'
    }

    file_path = 'output.xml'  # Ścieżka do pliku, gdzie mają być zapisane dane

    # Zapisywanie danych do pliku XML
    save_xml_file(data, file_path)

if __name__ == '__main__':
    main()