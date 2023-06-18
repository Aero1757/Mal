import tkinter as tk

def show_message():
    message = "Witaj, świat!"
    label.config(text=message)

# Tworzenie głównego okna
window = tk.Tk()

# Ustawienie tytułu okna
window.title("Mój Program z UI")

# Utworzenie etykiety
label = tk.Label(window, text="Kliknij przycisk, aby wyświetlić wiadomość")
label.pack(pady=10)

# Utworzenie przycisku
button = tk.Button(window, text="Kliknij mnie", command=show_message)
button.pack()

# Uruchomienie pętli zdarzeń
window.mainloop()