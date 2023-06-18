import tkinter as tk
import threading

def load_data():
    # Symulacja wczytywania danych
    # Tu możesz umieścić odpowiedni kod wczytywania danych z pliku

    # Wywołanie funkcji po wczytaniu danych
    data_loaded_callback()

def save_data():
    # Symulacja zapisu danych
    # Tu możesz umieścić odpowiedni kod zapisu danych do pliku

    # Wywołanie funkcji po zapisie danych
    data_saved_callback()

def data_loaded_callback():
    # Funkcja wywoływana po wczytaniu danych
    # Tutaj możesz umieścić kod obsługujący zdarzenie wczytania danych
    print("Dane zostały wczytane")

def data_saved_callback():
    # Funkcja wywoływana po zapisaniu danych
    # Tutaj możesz umieścić kod obsługujący zdarzenie zapisu danych
    print("Dane zostały zapisane")

def load_data_async():
    # Utworzenie wątku dla wczytywania danych
    thread = threading.Thread(target=load_data)
    thread.start()

def save_data_async():
    # Utworzenie wątku dla zapisu danych
    thread = threading.Thread(target=save_data)
    thread.start()

# Tworzenie głównego okna
window = tk.Tk()

# Ustawienie tytułu okna
window.title("Mój Program z UI")

# Utworzenie przycisków
load_button = tk.Button(window, text="Wczytaj dane", command=load_data_async)
load_button.pack(pady=10)

save_button = tk.Button(window, text="Zapisz dane", command=save_data_async)
save_button.pack()

# Uruchomienie pętli zdarzeń
window.mainloop()