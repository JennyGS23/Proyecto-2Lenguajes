import tkinter as tk
from tkinter import ttk
from controller_Main import DatabaseConnection
from model_MealComboDAO import ComboMealDAO
from model_PrologInterpreter import obtener_combinaciones_prolog


connection_string = DatabaseConnection()

class ComboMealView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menu Combo")
        self.geometry("900x500")

        label = tk.Label(self, text="MENU COMBO")
        label.pack()


        meal_dao = ComboMealDAO(connection_string)
        # Obtener las comidas de la base de datos
        meals = meal_dao.getMeal()

        # Listbox para mostrar los resultados
        frame_listbox = tk.Frame(self)
        frame_listbox.pack()
        self.listbox = tk.Listbox(frame_listbox, width=200, height=15)
        self.listbox.pack()
        for meal in meals:
            self.listbox.insert(tk.END, f"ID: {meal.getId()}, Drink: {meal.getDrink()}, Protein: {meal.getProtein()}, SideDish: {meal.getSideDish()}, Dessert: {meal.getDessert()}, Price: {meal.getPrice()},")

        
        self.selected_option = tk.StringVar()  # Variable para almacenar la selección del Listbox

        # Botón ordenar
        btnOrder = tk.Button(self, text="Ordenar combo", command=self.guardar_seleccion)
        btnOrder.pack()

    def guardar_seleccion(self):
        # Obtén la selección actual del Listbox
        selected_item = self.listbox.get(tk.ACTIVE)

        # Almacena la selección en la variable selected_option
        self.selected_option.set(selected_item)

        # Cierra la ventana
        self.destroy()



   

