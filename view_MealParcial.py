import tkinter as tk
from tkinter import ttk
from controller_Main import DatabaseConnection
from model_MealParcialDAO import ParcialMealDAO
import io

connection_string = DatabaseConnection()

class ParcialMealView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menu Parcial")
        self.geometry("900x500")

        label = tk.Label(self, text="MENU PARCIAL")
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
            self.listbox.insert(tk.END, f"ID: {meal.getId()}, Protein: {meal.getProtein()}, SideDish: {meal.getSideDish()}, Price: {meal.getPrice()} , Calorie: {meal.getCalorie()}")

        
        self.selected_option = tk.StringVar()  # Variable para almacenar la selección del Listbox

        # Botón ordenar
        btnOrder = tk.Button(self, text="Ordenar combo", command=self.guardar_seleccion)
        btnOrder.pack()

    def guardar_seleccion(self):
        # Obtén la selección actual del Listbox
        selected_item = self.listbox.get(tk.ACTIVE)

        with io.open("seleccionParcial.txt", "a", encoding="utf-8") as file:
            file.write(selected_item + "\n")

        # Almacena la selección en la variable selected_option
        self.selected_option.set(selected_item)

        # Cierra la ventana
        self.destroy()



   

