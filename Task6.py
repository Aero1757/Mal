import xml.etree.ElementTree as ET

def load_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print(f'Plik "{file_path}" nie istnieje.')
    except ET.ParseError as e:
        print(f'Błąd wczytywania pliku XML: {str(e)}')

def main():
    file_path = 'data.xml'  # Ścieżka do pliku XML

    # Wczytywanie pliku XML
    xml_data = load_xml_file(file_path)

    if xml_data:
        # Jeśli plik XML jest poprawny, można przeprowadzić operacje na wczytanych danych
        print('Plik XML jest poprawny.')
        print('Wczytane dane:')
        print(ET.tostring(xml_data, encoding='utf-8').decode())

if __name__ == '__main__':
    main()