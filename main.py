import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import math
import pandas as pd
import matplotlib.pyplot as plt

class HydroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikacja Hydrogeologiczna")
        self.geometry("1500x600")

        self.create_menu()

        self.project_frame = ProjectFrame(self)
        self.documentation_frame = DocumentationFrame(self)
        self.pumping_test_frame = PumpingTestFrame(self)
        self.welcome_window = WelcomeWindow(self)  # Dodaj okno powitalne
        self.welcome_window.lift()  # Podnieś okno powitalne na wierzch

    def create_menu(self):
        self.main_menu = tk.Menu(self)
        self.config(menu=self.main_menu)

        # Dodaj opcje "Projekt" do menu
        menu_projekt = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Projekt", menu=menu_projekt)
        menu_projekt.add_command(label="Obliczenia", command=self.show_project_frame)

        # Dodaj opcje "Dokumentacja" do menu
        menu_dokumentacja = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Dokumentacja", menu=menu_dokumentacja)
        menu_dokumentacja.add_command(label="Obliczenia (Zwierciadło swobodne w studni zupełnej)",
                                      command=self.show_documentation_frame)

        # Dodaj opcje "Proóbne pompowanie" do menu
        menu_pompowanie = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Proóbne pompowanie", menu=menu_pompowanie)
        menu_pompowanie.add_command(label="Wykres depresji", command=self.show_pumping_test_frame)

    def show_project_frame(self):
        self.documentation_frame.grid_forget()
        self.pumping_test_frame.grid_forget()
        self.project_frame.grid(row=0, column=0)

    def show_documentation_frame(self):
        self.project_frame.grid_forget()
        self.pumping_test_frame.grid_forget()
        self.documentation_frame.grid(row=0, column=0)

    def show_pumping_test_frame(self):
        self.project_frame.grid_forget()
        self.documentation_frame.grid_forget()
        self.pumping_test_frame.grid(row=0, column=0)

class WelcomeWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Witaj!")
        self.geometry("300x250")

        self.label = tk.Label(self, text="Witaj w aplikacji Hydrogeologicznej!")
        self.label.pack(pady=20)

        button_width = 30
        button_height = 2

        self.start_button1 = tk.Button(self, text="Projekt", command=self.start_app1, width=button_width, height=button_height)
        self.start_button1.pack()

        self.start_button2 = tk.Button(self, text="Dokumentacja", command=self.start_app2, width=button_width, height=button_height)
        self.start_button2.pack()

        self.start_button3 = tk.Button(self, text="Próbne Pompowanie", command=self.start_app3, width=button_width, height=button_height)
        self.start_button3.pack()

    def start_app1(self):
        self.destroy()  # Zamknij okno powitalne
        app.deiconify()
        app.show_project_frame()  # Przejdź do głównego interfejsu aplikacji

    def start_app2(self):
        self.destroy()  # Zamknij okno powitalne
        app.deiconify()
        app.show_documentation_frame()

    def start_app3(self):
        self.destroy()  # Zamknij okno powitalne
        app.deiconify()
        app.show_pumping_test_frame()

class HydroFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

    def create_widgets(self):
        pass

    def calculate(self):
        pass

class ProjectFrame(HydroFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Dodaj pola i etykiety dla ekranu Projekt

        # Pole na tytuł projektu
        self.Temat_label = tk.Label(self, text="Temat:", justify="right")
        self.Temat_label.grid(row=0, column=0, sticky="e")
        self.Temat_entry = tk.Entry(self)
        self.Temat_entry.grid(row=0, column=1)

        # Pole na lokalizację

        self.nr_dzialki_label = tk.Label(self, text="Nr działki:", justify="right")
        self.nr_dzialki_label.grid(row=1, column=0, sticky="e")
        self.nr_dzialki_entry = tk.Entry(self)
        self.nr_dzialki_entry.grid(row=1, column=1)


        self.miejscowosc_label = tk.Label(self, text="Miejscowość:", justify="right")
        self.miejscowosc_label.grid(row=2, column=0, sticky="e")
        self.miejscowosc_entry = tk.Entry(self)
        self.miejscowosc_entry.grid(row=2, column=1)

        self.gmina_label = tk.Label(self, text="Gmina:", justify="right")
        self.gmina_label.grid(row=3, column=0, sticky="e")
        self.gmina_entry = tk.Entry(self)
        self.gmina_entry.grid(row=3, column=1)

        self.powiat_label = tk.Label(self, text="Powiat:", justify="right")
        self.powiat_label.grid(row=4, column=0, sticky="e")
        self.powiat_entry = tk.Entry(self)
        self.powiat_entry.grid(row=4, column=1)

        self.wojewodztwo_label = tk.Label(self, text="Województwo:", justify="right")
        self.wojewodztwo_label.grid(row=5, column=0, sticky="e")
        self.wojewodztwo_entry = tk.Entry(self)
        self.wojewodztwo_entry.grid(row=5, column=1)

        self.zakladana_wydajnosc_label = tk.Label(self, text="Zakładana wydajność studni [m3/h]:", justify="right")
        self.zakladana_wydajnosc_label.grid(row=6, column=0, sticky="e")
        self.zakladana_wydajnosc_entry = tk.Entry(self)
        self.zakladana_wydajnosc_entry.grid(row=6, column=1)

        # Pole na średnicę otworu
        self.srednica_otworu_label = tk.Label(self, text="Średnica otworu [m]:", justify="right")
        self.srednica_otworu_label.grid(row=7, column=0, sticky="e")
        self.srednica_otworu_entry = tk.Entry(self)
        self.srednica_otworu_entry.grid(row=7, column=1)

        # Pole na długość części roboczej filtra
        self.dlugosc_filtru_label = tk.Label(self, text="Długość części roboczej filtra [m]:", justify="right")
        self.dlugosc_filtru_label.grid(row=8, column=0, sticky="e")
        self.dlugosc_filtru_entry = tk.Entry(self)
        self.dlugosc_filtru_entry.grid(row=8, column=1)

        # Pole na współczynnik filtracji
        self.wspolczynnik_filtracji_label = tk.Label(self,
                                                text="Współczynnik filtracji w rejonie projektowanego ujęcia [m/h]:", justify="right")
        self.wspolczynnik_filtracji_label.grid(row=9, column=0, sticky="e")
        self.wspolczynnik_filtracji_entry = tk.Entry(self)
        self.wspolczynnik_filtracji_entry.grid(row=9, column=1)

        # Pole na grubość warstwy wodonośnej
        self.grubosc_warstwy_wodnosnej_label = tk.Label(self, text="Miąższość warstwy wodonośnej [m]:", justify="right")
        self.grubosc_warstwy_wodnosnej_label.grid(row=10, column=0, sticky="e")
        self.grubosc_warstwy_wodnosnej_entry = tk.Entry(self)
        self.grubosc_warstwy_wodnosnej_entry.grid(row=10, column=1)

        # Pole na parametr liczbowy
        self.parametr_liczbowy_label = tk.Label(self, text="Parametr liczbowy dla warstwy wodonośnej (1 - 6):", justify="right")
        self.parametr_liczbowy_label.grid(row=11, column=0, sticky="e")
        self.parametr_liczbowy_entry = tk.Entry(self)
        self.parametr_liczbowy_entry.grid(row=11, column=1)

        # Pole na projektowaną wydajność jednostkową
        self.projektowana_wydajnosc_jednostkowa_label = tk.Label(self,
                                                            text="Projektowana wydajność jednostkowa [m3/h/1mS]:", justify="right")
        self.projektowana_wydajnosc_jednostkowa_label.grid(row=12, column=0, sticky="e")
        self.projektowana_wydajnosc_jednostkowa_entry = tk.Entry(self)
        self.projektowana_wydajnosc_jednostkowa_entry.grid(row=12, column=1)

        # Pozostałe pola i przyciski dla Projekt
        # ...

        self.oblicz_button = tk.Button(self, text="Oblicz", command=self.calculate, width=15, height=1)
        self.oblicz_button.grid(row=13, columnspan=3)

        # Wyświetl wyniki na ekranie Projekt
        self.wyniki_text = tk.Label(self, text="", justify="left")
        self.wyniki_text.grid(row=14, columnspan=2)

    def calculate(self):
        try:
            # Pobierz dane z pól tekstowych
            zakladana_wydajnosc = float(self.zakladana_wydajnosc_entry.get())
            srednica_otworu = float(self.srednica_otworu_entry.get())
            dlugosc_filtru = float(self.dlugosc_filtru_entry.get())
            wspolczynnik_filtracji = float(self.wspolczynnik_filtracji_entry.get())
            grubosc_warstwy_wodnosnej = float(self.grubosc_warstwy_wodnosnej_entry.get())
            parametr_liczbowy = float(self.parametr_liczbowy_entry.get())
            projektowana_wydajnosc_jednostkowa = float(self.projektowana_wydajnosc_jednostkowa_entry.get())

            # Pobierz tytuł projektu i lokalizację
            Temat = self.Temat_entry.get()
            nr_dzialki = self.nr_dzialki_entry.get()
            miejscowosc = self.miejscowosc_entry.get()
            gmina = self.gmina_entry.get()
            powiat = self.powiat_entry.get()
            wojewodztwo = self.wojewodztwo_entry.get()

            # Wykonaj obliczenia
            powierzchnia_filtracji = (3.14 * srednica_otworu * dlugosc_filtru)
            dopuszczalna_predkosc_wlotowa = 19.6 * math.sqrt(float(wspolczynnik_filtracji * 24))
            dopuszczalna_wydajnosc_studni = powierzchnia_filtracji * (dopuszczalna_predkosc_wlotowa / 24)
            przewodnosc_warstwy = wspolczynnik_filtracji * grubosc_warstwy_wodnosnej
            optymalna_wydajnosc_studni = parametr_liczbowy * przewodnosc_warstwy
            projektowana_depresja = (zakladana_wydajnosc / projektowana_wydajnosc_jednostkowa)

            # Wyświetl wyniki
            self.wyniki_text.config(text=f"Temat: {Temat}\n"f"Nr działki: {nr_dzialki}\n"f"Miejscowość: {miejscowosc}\n"f"Gmina: {gmina}\n"f"Powiat: {powiat}\n"f"Województwo: {wojewodztwo}\n"f"Powierzchnia filtracji [m2]: {powierzchnia_filtracji:.2f}\n"
                                            f"Dopuszczalna prędkość wlotowa do filtra [m/h]: {dopuszczalna_predkosc_wlotowa:.2f}\n"
                                            f"Dopuszczalna wydajność studni [m3/h]: {dopuszczalna_wydajnosc_studni:.2f}\n"
                                            f"Przewodność warstwy [m3/h]: {przewodnosc_warstwy:.2f}\n"
                                            f"Optymalna wydajność studni [m3/h]: {optymalna_wydajnosc_studni:.2f}\n"
                                            f"Projektowana depresja [m]: {projektowana_depresja:.2f}")
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawne wartości liczbowe")

class DocumentationFrame(HydroFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Dodaj pola i etykiety dla ekranu Dokumentacja
        pass

    def calculate(self):
        # Implementacja obliczeń dla ekranu Dokumentacja
        pass

class PumpingTestFrame(HydroFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.load_data_button = tk.Button(self, text="Wczytaj dane z pliku", command=self.load_data)
        self.load_data_button.pack()

        self.convert_button = tk.Button(self, text="Konwertuj dane", command=self.convert_data)
        self.convert_button.pack()

        self.data = None  # Inicjalizacja zmiennej data

        # Kontener dla tabeli z marginesem z lewej strony
        table_container = tk.Frame(self)
        table_container.pack(fill="both", expand=True)

        # Margines z lewej strony
        left_margin = tk.Label(table_container, text="", width=10)
        left_margin.pack(side="left", fill="y")

        self.data_table_scroll = tk.Scrollbar(table_container, orient="vertical")
        self.data_table_scroll.pack(side="right", fill="y")

        self.data_table = ttk.Treeview(table_container, yscrollcommand=self.data_table_scroll.set)
        self.data_table["columns"] = ("#", "Date", "Time", "ms", "LEVEL", "TEMPERATURE")
        self.data_table.heading("#1", text="#")
        self.data_table.heading("#2", text="Date")
        self.data_table.heading("#3", text="Time")
        self.data_table.heading("#4", text="ms")
        self.data_table.heading("#5", text="LEVEL")
        self.data_table.heading("#6", text="TEMPERATURE")
        self.data_table.pack(fill="both", expand=True)

        self.data_table_scroll.config(command=self.data_table.yview)

        # Etykieta do wyświetlania 11 pierwszych wierszy z pierwszej kolumny
        self.first_11_rows_label = tk.Label(self, text="")
        self.first_11_rows_label.pack()

        # Etykieta i pole tekstowe do wyboru zakresu wierszy do konwersji
        self.range_label = tk.Label(self, text="Wybierz zakres wierszy do konwersji (np. 5-10):")
        self.range_label.pack()
        self.range_entry = tk.Entry(self)
        self.range_entry.pack()

    def load_data(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Pliki CSV", "*.csv"), ("Pliki Excel", "*.xlsx"), ("Pliki TXT", "*.txt")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path, encoding="ISO-8859-1", parse_dates=[1], header=None, names=["Date", "Time", "ms", "LEVEL", "TEMPERATURE"], skiprows=11)  # Wczytaj dane z pliku CSV
                self.data["#"] = range(1, len(self.data) + 1)  # Dodaj numerację porządkową
                messagebox.showinfo("Sukces", "Dane wczytane pomyślnie.")
                self.display_data()  # Wywołaj funkcję do wyświetlenia danych w tabeli
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd wczytywania danych: {str(e)}")

    def display_data(self):
        # Wyczyść tabelę
        for row in self.data_table.get_children():
            self.data_table.delete(row)

        # Wstaw dane do tabeli
        for i, row in self.data.iterrows():
            self.data_table.insert("", "end",
                                   values=(row["#"], row["Date"], row["Time"], row["ms"], row["LEVEL"], row["TEMPERATURE"]))

    def convert_data(self):
        if self.data is not None:
            # Pobierz zakres wierszy do konwersji
            range_str = self.range_entry.get()
            try:
                start, end = map(int, range_str.split("-"))
                if start < 1 or end > len(self.data):
                    raise ValueError("Nieprawidłowy zakres wierszy.")
            except ValueError as e:
                messagebox.showerror("Błąd", f"Nieprawidłowy zakres wierszy: {str(e)}")
                return

                # Konwertuj kolumnę "Time" na liczbę
            self.data["Time"] = self.data["Time"].str.replace(',', '', regex=True)  # Usuń przecinki w czasie
            self.data["Time"] = pd.to_numeric(self.data["Time"], errors='coerce')

            # Konwertuj kolumnę "LEVEL" na liczbę
            self.data["LEVEL"] = self.data["LEVEL"].str.replace(',', '.', regex=True)
            self.data["LEVEL"] = pd.to_numeric(self.data["LEVEL"], errors='coerce')

            # Odejmij od kolumny "LEVEL" wartość pierwszego wiersza
            self.data.loc[start - 1:end - 1, "LEVEL"] -= self.data.loc[start - 1, "LEVEL"]


            # Stwórz nową tabelę z przekonwertowanymi danymi
            converted_data = self.data.iloc[start - 1:end]

            # Debugging: Wyświetl przekształcone dane
            print("Przekształcone dane:")
            print(converted_data)

            # Wyświetl nową tabelę pod pierwszą tabelą
            self.display_converted_data(converted_data)
        else:
            messagebox.showerror("Błąd", "Wczytaj dane przed konwersją.")

    def display_converted_data(self, data):
        # Tworzenie nowego okna do wyświetlenia przekonwertowanych danych
        converted_data_window = tk.Toplevel(self)
        converted_data_window.title("Przekonwertowane dane")

        # Kontener dla tabeli z marginesem z lewej strony
        table_container = tk.Frame(converted_data_window)
        table_container.pack(fill="both", expand=True)

        # Margines z lewej strony
        left_margin = tk.Label(table_container, text="", width=10)
        left_margin.pack(side="left", fill="y")

        converted_data_table_scroll = tk.Scrollbar(table_container, orient="vertical")
        converted_data_table_scroll.pack(side="right", fill="y")

        converted_data_table = ttk.Treeview(table_container, yscrollcommand=converted_data_table_scroll.set)
        converted_data_table["columns"] = ("#", "Date", "Time", "LEVEL", "TEMPERATURE")
        converted_data_table.heading("#1", text="#")
        converted_data_table.heading("#2", text="Date")
        converted_data_table.heading("#3", text="Time")
        converted_data_table.heading("#4", text="LEVEL")
        converted_data_table.heading("#5", text="TEMPERATURE")
        converted_data_table.pack(fill="both", expand=True)

        converted_data_table_scroll.config(command=converted_data_table.yview)


if __name__ == "__main__":
    app = HydroApp()
    app.withdraw()  # Ukryj główne okno aplikacji na początek
    app.mainloop()