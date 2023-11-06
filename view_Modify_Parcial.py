import tkinter as tk
import tkinter

from controller_Main import DatabaseConnection
from model_MealParcialDAO import ParcialMealDAO 


# Establish a connection to the database
connection_string = DatabaseConnection()
class Modify_Parcial_View(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones para Modificar")
        self.geometry("900x500")

        label = tk.Label(self, text="Escoge el menú donde deseas modificar el precio")
        label.pack()


        meal_dao = ParcialMealDAO(connection_string)
        # Obtener las comidas de la base de datos
        meals = meal_dao.getMeal()

        # Listbox para mostrar los resultados
        frame_listbox = tk.Frame(self)
        frame_listbox.pack()
        self.listbox = tk.Listbox(frame_listbox, width=200, height=15)
        self.listbox.pack()
        for meal in meals:
            self.listbox.insert(tk.END, f"ID: {meal.getId()}, Protein: {meal.getProtein()}, SideDish: {meal.getSideDish()}, Price: {meal.getPrice()}, Calorie: {meal.getCalorie()}")

        
        self.selected_option = tk.StringVar()  # Variable para almacenar la selección del Listbox

        self.selected_Price = tk.StringVar()  # Variable para almacenar la selección
        frame_price = tk.Frame(self)
        frame_price.pack()
        lblPrice = tk.Label(frame_price, text="Nuevo Precio: ")
        lblPrice.pack(side="left")
        comboPrice = tk.Entry(frame_price, textvariable=self.selected_Price)
        comboPrice.pack(side="left")

        # Botón ordenar
        btnOrder = tk.Button(self, text="Modificar Parcial", command=self.guardar_seleccion)
        btnOrder.pack()

    def guardar_seleccion(self):
        # Obtener el índice seleccionado en el Listbox
        selected_index = self.listbox.curselection()[0]

        # Obtener la línea de texto seleccionada
        selected_line = self.listbox.get(selected_index)

        # Analizar la línea de texto para obtener los valores
        values = selected_line.split(", ")  # Suponiendo que los valores estén separados por comas y un espacio
        protein_value = values[1].split(": ")[1]
        side_dish_value = values[2].split(": ")[1]
        price_selection = self.selected_Price.get()
        calorie_value = values[3].split(": ")[1]

        # Llamar a delete_New_Combo con los valores seleccionados
        self.Modify_Parcial(protein_value, side_dish_value, price_selection, calorie_value)

    def Modify_Parcial(self, protein, side_dish, price, calorie):
        database = ParcialMealDAO(connection_string)

        # Utiliza los valores recibidos como parámetros
        # para eliminar la combinación deseada
        database.updatePrice(protein, side_dish, price, calorie)