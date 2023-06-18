import xml.etree.ElementTree as ET

# Parsowanie danych z pliku XML
tree = ET.parse("data.xml")
root = tree.getroot()

# Przykład odczytu danych z pliku XML
for child in root:
    print(child.tag, child.attrib)

# Przykład tworzenia nowego elementu i dodawania go do drzewa XML
new_element = ET.Element("new_element")
new_element.text = "Hello, World!"
root.append(new_element)

# Zapis danych do pliku XML
tree.write("new_data.xml")