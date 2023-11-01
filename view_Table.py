import tkinter as tk
from tkinter import ttk

from view_MealHealthy import HealthyMealView

class TableView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pedir mesa")
        self.geometry("300x300")

        label = tk.Label(self, text="Pide una mesa")
        label.pack()

        # ComboBox cantSeats
        self.selected_drink = tk.StringVar()  # Variable para almacenar la selección
        frame_drink = tk.Frame(self)
        frame_drink.pack()
        lblDrink = tk.Label(frame_drink, text="Cantidad de asientos:")
        lblDrink.pack(side="left")
        comboDrink = ttk.Combobox(frame_drink, values=["1", "2", "3", "4", "5"], state="readonly", textvariable=self.selected_drink)
        comboDrink.pack(side="left")

        # ComboBox proteína
        self.selected_protein = tk.StringVar()  # Variable para almacenar la selección
        frame_protein = tk.Frame(self)
        frame_protein.pack()
        lblProtein = tk.Label(frame_protein, text="Pago unico:")
        lblProtein.pack(side="left")
        comboProtein = ttk.Combobox(frame_protein, values=["Si", "No"], state="readonly", textvariable=self.selected_protein)
        comboProtein.pack(side="left")

        # Botón calcular
        btnCalc = tk.Button(self, text="Pedir", command=self.mostrar_opciones)
        btnCalc.pack()

    def mostrar_opciones(self):
        # Aquí pueHealthyMealView selecciones de los ComboBox y enviarlas al controlador
        drink_selection = self.selected_drink.get()
        protein_selection = self.selected_protein.get()
        # Obtener selecciones de otros ComboBoxes de la misma manera

        # Aquí debes procesar las selecciones como lo necesites
        # Por ahora, solo lo mostraré en el Listbox como ejemplo
        #self.listbox.delete(0, tk.END)  # Borrar elementos anteriores en el Listbox
        #self.listbox.insert(tk.END, f"Selección de bebida: {drink_selection}")
        #self.listbox.insert(tk.END, f"Selección de proteína: {protein_selection}")
        # Mostrar selecciones de otros ComboBoxes de la misma manera
        return drink_selection, protein_selection

