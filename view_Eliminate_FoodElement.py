import tkinter as tk
import tkinter
from controller_Main import DatabaseConnection

from model_FoodElementDAO import FoodElementDAO 

# Establish a connection to the database
connection_string = DatabaseConnection()

class Eliminate_FoodElement_View(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Elimiar Elemento Comida")
        self.geometry("900x500")

        label = tk.Label(self, text="Ingresa el Nombre Del elemento comida a eliminar")
        label.pack()


        self.selected_Name = tk.StringVar()  # Variable para almacenar la selección
        frame_name = tk.Frame(self)
        frame_name.pack()
        lblName = tk.Label(frame_name, text="Nombre: ")
        lblName.pack(side="left")
        comboName = tk.Entry(frame_name, textvariable=self.selected_Name)
        comboName.pack(side="left")



        btnOrder = tk.Button(self, text="Eliminar elemento", command=self.eliminate_Element)
        btnOrder.pack()

    def eliminate_Element(self):
        database = FoodElementDAO(connection_string)

        Name_selection = self.selected_Name.get()
        print(Name_selection)

        database.deleteCaloriesByName(Name_selection)
        database.deleteFoodElementByName(Name_selection)
        database.deletePriceByName(Name_selection)
   