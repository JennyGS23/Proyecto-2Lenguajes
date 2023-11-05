import tkinter as tk
import tkinter
from controller_Main import DatabaseConnection

from model_MealParcialDAO import ParcialMealDAO 
connection_string = DatabaseConnection()

class Add_Parcial_View(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Agregar elementos Parcial")
        self.geometry("900x500")

        label = tk.Label(self, text="Ingresa los elementos para agregar")
        label.pack()


        self.selected_Proteins = tk.StringVar()  # Variable para almacenar la selección
        frame_proteins = tk.Frame(self)
        frame_proteins.pack()
        lblProteins = tk.Label(frame_proteins, text="Nombre de la Proteina: ")
        lblProteins.pack(side="left")
        comboProteins = tk.Entry(frame_proteins, textvariable=self.selected_Proteins)
        comboProteins.pack(side="left")

        self.selected_SideDish = tk.StringVar()  # Variable para almacenar la selección
        frame_sideDish = tk.Frame(self)
        frame_sideDish.pack()
        lblSideDish = tk.Label(frame_sideDish, text="Nombre del acompañamiento: ")
        lblSideDish.pack(side="left")
        comboSideDish = tk.Entry(frame_sideDish, textvariable=self.selected_SideDish)
        comboSideDish.pack(side="left")


        self.selected_Price = tk.StringVar()  # Variable para almacenar la selección
        frame_price = tk.Frame(self)
        frame_price.pack()
        lblPrice = tk.Label(frame_price, text="Costo total: ")
        lblPrice.pack(side="left")
        comboPrice = tk.Entry(frame_price, textvariable=self.selected_Price)
        comboPrice.pack(side="left")

        # Botón ordenar
        btnNewCombo = tk.Button(self, text="Guardar nuevo Parcial", command= self.save_New_Parcial)
        btnNewCombo.pack()

    def save_New_Parcial(self):
        database = ParcialMealDAO(connection_string)

        protein_selection = self.selected_Proteins.get()
        side_dish_selection = self.selected_SideDish.get()
        price_selection = self.selected_Price.get()
        #print(drink_selection, protein_selection, side_dish_selection, dessert_selection, price_selection)

        database.setMeal(protein_selection, side_dish_selection,  price_selection)