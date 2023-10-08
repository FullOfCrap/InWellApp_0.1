import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import math
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta


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

        self.start_button1 = tk.Button(self, text="Projekt", command=self.start_app1, width=button_width,
                                       height=button_height)
        self.start_button1.pack()

        self.start_button2 = tk.Button(self, text="Dokumentacja", command=self.start_app2, width=button_width,
                                       height=button_height)
        self.start_button2.pack()

        self.start_button3 = tk.Button(self, text="Próbne Pompowanie", command=self.start_app3, width=button_width,
                                       height=button_height)
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
                                                     text="Współczynnik filtracji w rejonie projektowanego ujęcia [m/h]:",
                                                     justify="right")
        self.wspolczynnik_filtracji_label.grid(row=9, column=0, sticky="e")
        self.wspolczynnik_filtracji_entry = tk.Entry(self)
        self.wspolczynnik_filtracji_entry.grid(row=9, column=1)

        # Pole na grubość warstwy wodonośnej
        self.grubosc_warstwy_wodnosnej_label = tk.Label(self, text="Miąższość warstwy wodonośnej [m]:", justify="right")
        self.grubosc_warstwy_wodnosnej_label.grid(row=10, column=0, sticky="e")
        self.grubosc_warstwy_wodnosnej_entry = tk.Entry(self)
        self.grubosc_warstwy_wodnosnej_entry.grid(row=10, column=1)

        # Pole na parametr liczbowy
        self.parametr_liczbowy_label = tk.Label(self, text="Parametr liczbowy dla warstwy wodonośnej (1 - 6):",
                                                justify="right")
        self.parametr_liczbowy_label.grid(row=11, column=0, sticky="e")
        self.parametr_liczbowy_entry = tk.Entry(self)
        self.parametr_liczbowy_entry.grid(row=11, column=1)

        # Pole na projektowaną wydajność jednostkową
        self.projektowana_wydajnosc_jednostkowa_label = tk.Label(self,
                                                                 text="Projektowana wydajność jednostkowa [m3/h/1mS]:",
                                                                 justify="right")
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
            self.wyniki_text.config(
                text=f"Temat: {Temat}\n"f"Nr działki: {nr_dzialki}\n"f"Miejscowość: {miejscowosc}\n"f"Gmina: {gmina}\n"f"Powiat: {powiat}\n"f"Województwo: {wojewodztwo}\n"f"Powierzchnia filtracji [m2]: {powierzchnia_filtracji:.2f}\n"
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
        self.data = None

    def create_widgets(self):
        self.load_data_button = tk.Button(self, text="Wczytaj dane z pliku", command=self.load_data)
        self.load_data_button.pack()

        self.draw_chart_button = tk.Button(self, text="Narysuj wykres", command=self.draw_chart)
        self.draw_chart_button.pack()

        self.data_entry_frame = tk.Frame(self)
        self.data_entry_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.label_wydajnosc_pompowania = tk.Label(self.data_entry_frame, text="Wydajność pompowania pomiarowego:")
        self.label_wydajnosc_pompowania.pack()
        self.entry_wydajnosc_pompowania = tk.Entry(self.data_entry_frame)
        self.entry_wydajnosc_pompowania.pack()

        self.label_depresja_rzeczywista = tk.Label(self.data_entry_frame, text="Depresja rzeczywista w studni:")
        self.label_depresja_rzeczywista.pack()
        self.entry_depresja_rzeczywista = tk.Entry(self.data_entry_frame)
        self.entry_depresja_rzeczywista.pack()

        self.label_miazszosc_warstwy = tk.Label(self.data_entry_frame, text="Miąższość warstwy wodonośnej:")
        self.label_miazszosc_warstwy.pack()
        self.entry_miazszosc_warstwy = tk.Entry(self.data_entry_frame)
        self.entry_miazszosc_warstwy.pack()

        self.label_parametrC = tk.Label(self.data_entry_frame, text="Parametr C:")
        self.label_parametrC.pack()
        self.entry_parametrC = tk.Entry(self.data_entry_frame)
        self.entry_parametrC.pack()

        self.calculate_button = tk.Button(self.data_entry_frame, text="Oblicz", command=self.calculate)
        self.calculate_button.pack()

        # Data table frame
        data_table_frame = tk.Frame(self)
        data_table_frame.pack(fill="both", expand=True)

        # Margines z lewej strony
        left_margin = tk.Label(data_table_frame, text="", width=10)
        left_margin.pack(side="left", fill="y")

        self.data_table = ttk.Treeview(data_table_frame, columns=("Czas", "Depresja_opad", "Depresja_wznios"))
        self.data_table.heading("Czas", text="Czas")
        self.data_table.heading("Depresja_opad", text="Depresja opad")
        self.data_table.heading("Depresja_wznios", text="Depresja wznios")
        self.data_table.pack(side="left", fill="both", expand=True)

        self.result_label = tk.Label(self.data_entry_frame, text="")
        self.result_label.pack()

    def load_data(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Pliki CSV", "*.csv"), ("Pliki Excel", "*.xlsx"), ("Pliki TXT", "*.txt")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                messagebox.showinfo("Sukces", "Dane wczytane pomyślnie.")
                self.display_data()
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd wczytywania danych: {str(e)}")

    def draw_chart(self):
        if self.data is not None:
            plt.scatter(self.data["Czas"], self.data["Depresja_roznica_opad"], label='opad')
            plt.scatter(self.data["Czas"], self.data["Depresja_roznica_wznios"], label='wznios')

            # Zaznacz punkt przegięcia na wykresie dla depresja_opad
            punkt_przegiecia_opad = self.find_inflection_point(self.data["Czas"], self.data["Depresja_roznica_opad"])
            if punkt_przegiecia_opad:
                czas_opad, depresja_opad = punkt_przegiecia_opad
                plt.scatter(czas_opad, depresja_opad, color='red', label='Punkt przegięcia opad')
                result_text_opad = f'Punkt przegięcia opad: Czas={czas_opad}, Depresja_opad={depresja_opad:.2f}'
                self.result_label.config(text=result_text_opad)
                print(result_text_opad)

                # Dodaj etykietę (annotation) z wartością punktu przegięcia opad
                plt.annotate(
                    f'Punkt przegięcia opad: Depresja_opad={depresja_opad:.2f}',
                    (czas_opad, depresja_opad),
                    textcoords="offset points", xytext=(0, 10), ha='center')

            # Zaznacz punkt przegięcia na wykresie dla depresja_wznios
            punkt_przegiecia_wznios = self.find_inflection_point(self.data["Czas"],
                                                                 self.data["Depresja_roznica_wznios"])
            if punkt_przegiecia_wznios:
                czas_wznios, depresja_wznios = punkt_przegiecia_wznios
                plt.scatter(czas_wznios, depresja_wznios, color='green', label='Punkt przegięcia wznios')
                result_text_wznios = f'Punkt przegięcia wznios: Czas={czas_wznios}, Depresja_wznios={depresja_wznios:.2f}'
                self.result_label.config(text=result_text_wznios)
                print(result_text_wznios)

                # Dodaj etykietę (annotation) z wartością punktu przegięcia wznios
                plt.annotate(
                    f'Punkt przegięcia wznios: Depresja_wznios={depresja_wznios:.2f}',
                    (czas_wznios, depresja_wznios),
                    textcoords="offset points", xytext=(0, 10), ha='center')

            plt.xlabel("Czas t [h]")
            plt.ylabel("Depresja [m]")
            plt.title("Wykres depresji zwierciadła wody w czasie (na podstawie Depresja_roznica)")
            plt.legend()
            plt.xscale('log')  # Ustaw skalę logarytmiczną na osi X
            plt.grid(True)  # Dodaj siatkę na wykresie
            plt.grid(which='both', linestyle='--', linewidth=0.5)
            plt.show()
        else:
            messagebox.showerror("Błąd", "Wczytaj dane przed narysowaniem wykresu.")

    def find_inflection_point(self, x, y):
        for i in range(1, len(y) - 1):
            if y[i - 1] > y[i] < y[i + 1]:
                return x[i], y[i]
        return None

    def display_data(self):
        # Wyczyść tabelę
        for row in self.data_table.get_children():
            self.data_table.delete(row)

        # Wstaw dane do tabeli
        for i, row in self.data.iterrows():
            self.data_table.insert("", "end",
                                   values=(row["Czas"], row["Depresja_roznica_opad"], row["Depresja_roznica_wznios"]))

    def calculate(self):
        wydajnosc_pompowania = float(self.entry_wydajnosc_pompowania.get())
        depresja_rzeczywista = float(self.entry_depresja_rzeczywista.get())
        miazszosc_warstwy = float(self.entry_miazszosc_warstwy.get())
        parametrC = float(self.entry_parametrC.get())

        Przewodnosc_warstwy = (0.183 * wydajnosc_pompowania) / parametrC
        wspolczynnik_filtracji = Przewodnosc_warstwy / miazszosc_warstwy

        self.result_label.config(text=f"Przewodność warstwy (T) [m2/h]: {Przewodnosc_warstwy:.2f}" +
                                      f"\nWspółczynnik filtracji (K) [m/h]: {wspolczynnik_filtracji:.2f}")


if __name__ == "__main__":
    app = HydroApp()
    app.withdraw()  # Ukryj główne okno aplikacji na początek
    app.mainloop()