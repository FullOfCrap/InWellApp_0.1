import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,  NavigationToolbar2Tk
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D

import datetime
from datetime import timedelta


class HydroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikacja Hydrogeologiczna")
        self.geometry("1500x900")

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


class Cursor:
    def __init__(self, ax, useblit=True, **lineprops):
        self.ax = ax
        self.figure = ax.figure
        self.canvas = self.figure.canvas
        self.useblit = useblit
        self.lineprops = lineprops

        self.active = False  # Whether the cursor is active (drawing) or not
        self.points = []     # List to store the drawn points

        self._init_cursor()

    def _init_cursor(self):
        self.line = Line2D([0], [0], marker='o', **self.lineprops)
        self.line.set_visible(False)
        self.ax.add_line(self.line)

        if self.useblit:
            self.canvas.mpl_connect('button_press_event', self.on_press)
            self.canvas.mpl_connect('button_release_event', self.on_release)
            self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        else:
            self.canvas.mpl_connect('button_press_event', self.on_click)

    def on_press(self, event):
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.line.set_data([x], [y])
            self.line.set_visible(True)
            self.canvas.draw()
            self.active = True

    def on_motion(self, event):
        if self.active and event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.line.set_data([x], [y])
            self.canvas.draw()

    def on_release(self, event):
        if self.active:
            x, y = event.xdata, event.ydata
            self.points.append((x, y))
            self.active = False

    def on_click(self, event):
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.points.append((x, y))

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

class Cursor:
    def __init__(self, ax, useblit=True, **lineprops):
        self.ax = ax
        self.canvas = ax.figure.canvas
        self.visible = True

        self.horizontal_line = Line2D([], [], **lineprops)
        self.vertical_line = Line2D([], [], **lineprops)
        self.ax.add_line(self.horizontal_line)
        self.ax.add_line(self.vertical_line)

        self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas.mpl_connect('button_press_event', self.on_mouse_press)

        self.points = []  # Dodaj atrybut points

        self._init_cursor()
    def _init_cursor(self):
        self.line = Line2D([0], [0], marker='o', **self.lineprops)
        self.line.set_visible(False)
        self.ax.add_line(self.line)

        if self.useblit:
            self.canvas.mpl_connect('button_press_event', self.on_press)
            self.canvas.mpl_connect('button_release_event', self.on_release)
            self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        else:
            self.canvas.mpl_connect('button_press_event', self.on_click)

    def on_mouse_move(self, event):
        if not self.visible:
            return
        if event.inaxes != self.ax:
            return
        x, y = event.xdata, event.ydata
        self.horizontal_line.set_data([self.ax.get_xlim()[0], self.ax.get_xlim()[1]], [y, y])
        self.vertical_line.set_data([x, x], [self.ax.get_ylim()[0], self.ax.get_ylim()[1]])
        self.canvas.draw()

    def on_mouse_press(self, event):
        if not self.visible:
            return
        if event.inaxes != self.ax:
            return
        x, y = event.xdata, event.ydata
        self.points.append((x, y))
        self.active = False

class PumpingTestFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.data = None
        self.points_opad = []  # Przechowuj punkty opad na wykresie
        self.points_wznios = []  # Przechowuj punkty wznios na wykresie
        self.create_plot_frame()

    def create_widgets(self):
        self.load_data_button = tk.Button(self, text="Wczytaj dane z pliku", command=self.load_data)
        self.load_data_button.pack()

        self.data_entry_frame = tk.Frame(self)
        self.data_entry_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.label_tytul_wykresu = tk.Label(self.data_entry_frame, text="Tytuł wykresu:")
        self.label_tytul_wykresu.pack()
        self.entry_tytul_wykresu = tk.Entry(self.data_entry_frame)
        self.entry_tytul_wykresu.pack()

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

        data_table_frame = tk.Frame(self)
        data_table_frame.pack(fill="both", expand=True)

        # Dodaj pionowy suwak
        self.data_table_scroll = tk.Scrollbar(data_table_frame, orient="vertical")
        self.data_table_scroll.pack(side="right", fill="y")

        left_margin = tk.Label(data_table_frame, text="", width=10)
        left_margin.pack(side="left", fill="y")

        # Utwórz ramkę na wykres
        self.plot_frame = tk.Frame(self)
        self.plot_frame.pack(side="left", padx=40, pady=60)  # Przesunięcie całej ramki w prawo o 20 pikseli

        # Ustawienie stylu dla tabeli
        style = ttk.Style()
        style.configure("Treeview", rowheight=30)  # Ustawienie wysokości wierszy

        self.data_table = ttk.Treeview(data_table_frame, columns=("Czas", "Depresja_opad", "Depresja_wznios"),
                                       show="headings")

        # Dodanie linii oddzielających kolumny
        self.data_table["style"] = "mystyle.Treeview"
        style.configure("mystyle.Treeview", rowheight=30, font=('Helvetica', 10), background="#E1E1E1")
        style.layout("mystyle.Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        # Przypisz suwak pionowy do tabeli
        self.data_table.config(yscrollcommand=self.data_table_scroll.set)
        self.data_table_scroll.config(command=self.data_table.yview)

        self.data_table.heading("Czas", text="Czas")
        self.data_table.heading("Depresja_opad", text="Depresja opad")
        self.data_table.heading("Depresja_wznios", text="Depresja wznios")

        for col in ("Czas", "Depresja_opad", "Depresja_wznios"):
            self.data_table.column(col, anchor="center")

        self.data_table.pack(fill="both", expand=True)

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


    def create_plot_frame(self):
        self.plot_frame = tk.Frame(self)
        self.plot_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    def draw_chart(self):
        if self.data is not None:
            tytul_wykresu = self.entry_tytul_wykresu.get()
            fig, ax = plt.subplots()

            # Rysuj punkty z listy self.points_opad i self.points_wznios
            opad_x = [point[0] for point in self.points_opad]
            opad_y = [point[1] for point in self.points_opad]
            wznios_x = [point[0] for point in self.points_wznios]
            wznios_y = [point[1] for point in self.points_wznios]

            # Tworzenie wykresu z punktami
            ax.scatter(opad_x, opad_y, label='opad', color='blue')
            ax.scatter(wznios_x, wznios_y, label='wznios', color='red')

            # Tworzenie wykresu
            ax.scatter(self.data["Czas"], self.data["Depresja_roznica_opad"], label='opad')
            ax.scatter(self.data["Czas"], self.data["Depresja_roznica_wznios"], label='wznios')
            ax.set_xlabel("Czas t [h]")
            ax.set_ylabel("Depresja [m]")
            ax.set_title(tytul_wykresu)
            ax.legend()
            ax.set_xscale('log')
            ax.grid(True)
            ax.grid(which='both', linestyle='--', linewidth=0.5)

            # Tworzenie obszaru wykresu
            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self.plot_frame)
            toolbar.update()
            toolbar.pack(side="top", fill="both", expand=True)

            # Tworzenie narzędzia do rysowania
            cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

            # Przycisk do włączania/wyłączania narzędzia do rysowania
            self.toggle_cursor_button = tk.Button(self.plot_frame, text="Włącz narzędzie do rysowania",
                                                  command=lambda: self.toggle_cursor(cursor))
            self.toggle_cursor_button.pack()
        else:
            messagebox.showerror("Błąd", "Wczytaj dane przed narysowaniem wykresu.")

    def toggle_cursor(self):
        if self.cursor.active:
            self.cursor.active = False
            self.toggle_cursor_button.config(text="Włącz narzędzie do rysowania")
        else:
            self.cursor.active = True
            self.toggle_cursor_button.config(text="Wyłącz narzędzie do rysowania")

    def add_point(self, event):
        if self.data is not None and event.xdata is not None and event.ydata is not None:
            x = event.xdata
            y = event.ydata
            if event.button == 1:
                self.cursor.points_opad.append((x, y))
            elif event.button == 3:
                self.cursor.points_wznios.append((x, y))
            self.draw_chart()

    def display_data(self):
        for row in self.data_table.get_children():
            self.data_table.delete(row)

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