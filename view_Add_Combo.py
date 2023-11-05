import tkinter as tk
import tkinter

from controller_Main import DatabaseConnection
from model_MealComboDAO import ComboMealDAO 

connection_string = DatabaseConnection()
class Add_Combo_View(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones para Agregar")
        self.geometry("900x500")

        label = tk.Label(self, text="Escoge el menú donde deseas agregar")
        label.pack()


        self.selected_Drink = tk.StringVar()  # Variable para almacenar la selección
        frame_drink = tk.Frame(self)
        frame_drink.pack()
        lblDrink = tk.Label(frame_drink, text="Nombre de la Bebida del combo:")
        lblDrink.pack(side="left")
        comboDrink = tk.Entry(frame_drink, textvariable=self.selected_Drink)
        comboDrink.pack(side="left")

        self.selected_Protein = tk.StringVar()  # Variable para almacenar la selección
        frame_proteins = tk.Frame(self)
        frame_proteins.pack()
        lblProteins = tk.Label(frame_proteins, text="Nombre de la Proteina del Combo:")
        lblProteins.pack(side="left")
        comboProteins = tk.Entry(frame_proteins, textvariable=self.selected_Protein)
        comboProteins.pack(side="left")

        self.selected_SideDish = tk.StringVar()  # Variable para almacenar la selección
        frame_sideDish = tk.Frame(self)
        frame_sideDish.pack()
        lblSideDish = tk.Label(frame_sideDish, text="Nombre del acompañamiento del Combo: ")
        lblSideDish.pack(side="left")
        comboSideDish = tk.Entry(frame_sideDish, textvariable=self.selected_SideDish)
        comboSideDish.pack(side="left")

        self.selected_Dessert = tk.StringVar()  # Variable para almacenar la selección
        frame_dessert = tk.Frame(self)
        frame_dessert.pack()
        lblDessert = tk.Label(frame_dessert, text="Nombre del Postre del Combo: ")
        lblDessert.pack(side="left")
        comboDessert = tk.Entry(frame_dessert, textvariable=self.selected_Dessert)
        comboDessert.pack(side="left")

        self.selected_Price = tk.StringVar()  # Variable para almacenar la selección
        frame_price = tk.Frame(self)
        frame_price.pack()
        lblPrice = tk.Label(frame_price, text="Costo total: ")
        lblPrice.pack(side="left")
        comboPrice = tk.Entry(frame_price, textvariable=self.selected_Price)
        comboPrice.pack(side="left")

        # Botón ordenar
        btnNewCombo = tk.Button(self, text="Guardar nuevo Combo", command= self.save_New_Combo)
        btnNewCombo.pack()
    

    def save_New_Combo(self):
        database = ComboMealDAO(connection_string)

        drink_selection = self.selected_Drink.get()
        protein_selection = self.selected_Protein.get()
        side_dish_selection = self.selected_SideDish.get()
        dessert_selection = self.selected_Dessert.get()
        price_selection = self.selected_Price.get()
        #print(drink_selection, protein_selection, side_dish_selection, dessert_selection, price_selection)

        database.setMeal(drink_selection, protein_selection, side_dish_selection, dessert_selection, price_selection)

    