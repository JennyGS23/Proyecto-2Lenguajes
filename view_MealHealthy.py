import tkinter as tk
from tkinter import ttk

class HealthyMealView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menu saludable")
        self.geometry("500x500")

        label = tk.Label(self, text="MENU SALUDABLE")
        label.pack()

        # ComboBox bebida
        self.selected_drink = tk.StringVar()  # Variable para almacenar la selección
        frame_drink = tk.Frame(self)
        frame_drink.pack()
        lblDrink = tk.Label(frame_drink, text="Tipo de Bebida:")
        lblDrink.pack(side="left")
        comboDrink = ttk.Combobox(frame_drink, values=["natural", "caliente", "carbonatada", "con_lácteo"], state="readonly", textvariable=self.selected_drink)
        comboDrink.pack(side="left")

        # ComboBox proteína
        self.selected_protein = tk.StringVar()  # Variable para almacenar la selección
        frame_protein = tk.Frame(self)
        frame_protein.pack()
        lblProtein = tk.Label(frame_protein, text="Tipo de proteína:")
        lblProtein.pack(side="left")
        comboProtein = ttk.Combobox(frame_protein, values=["roja", "blanca", "marino"], state="readonly", textvariable=self.selected_protein)
        comboProtein.pack(side="left")

        # ComboBox extras
        frame_side_dish = tk.Frame(self)
        frame_side_dish.pack()
        lblSideDish = tk.Label(frame_side_dish, text="Tipo de acompañamiento:")
        lblSideDish.pack(side="left")
        comboSideDish = ttk.Combobox(frame_side_dish, values=["vegetales", "carbohidratos", "calientes"], state="readonly")
        comboSideDish.pack(side="left")

        # ComboBox postre
        frame_dessert = tk.Frame(self)
        frame_dessert.pack()
        lblDessert = tk.Label(frame_dessert, text="Tipo de postre:")
        lblDessert.pack(side="left")
        comboDesert = ttk.Combobox(frame_dessert, values=["sin_lácteo", "con_lácteo", "repostería"], state="readonly")
        comboDesert.pack(side="left")

        # ComboBox calorías
        frame_calories = tk.Frame(self)
        frame_calories.pack()
        lblCalories = tk.Label(frame_calories, text="Calorías máximas:")
        lblCalories.pack(side="left")
        comboCalories = tk.Entry(frame_calories)
        comboCalories.pack(side="left")

        # Botón calcular
        btnCalc = tk.Button(self, text="Ver opciones", command=self.mostrar_opciones)
        btnCalc.pack()

        # Listbox para mostrar los resultados
        frame_listbox = tk.Frame(self)
        frame_listbox.pack()
        self.listbox = tk.Listbox(frame_listbox, width=40, height=15)
        self.listbox.pack()


    def mostrar_opciones(self):
        # Aquí puedes obtener las selecciones de los ComboBox y enviarlas al controlador
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

