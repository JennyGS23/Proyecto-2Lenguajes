import tkinter as tk
import tkinter
from tkinter import ttk
from controller_Main import DatabaseConnection

from model_FoodElementDAO import FoodElementDAO 
# Establish a connection to the database
connection_string = DatabaseConnection()

class Modify_FoodElement_View(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Modificar")
        self.geometry("900x500")

        label = tk.Label(self, text="Ingresa el nombre del elemento que deseas modificar")
        label.pack()

        self.selected_Name = tk.StringVar()  # Variable para almacenar la selección
        frame_name = tk.Frame(self)
        frame_name.pack()
        lblName = tk.Label(frame_name, text="Nombre: ")
        lblName.pack(side="left")
        comboName = tk.Entry(frame_name, textvariable=self.selected_Name)
        comboName.pack(side="left")

        self.selected_dayMoment = tk.StringVar()  # Variable para almacenar la selección
        frameSeats = tk.Frame(self)
        frameSeats.pack()
        lblSeats = tk.Label(frameSeats, text="Momento del dia:")
        lblSeats.pack(side="left")
        comboSeats = ttk.Combobox(frameSeats, values=["desayuno", "almuerzo", "cena", "general"], state="readonly", textvariable=self.selected_dayMoment)
        comboSeats.pack(side="left")

        btnOrder = tk.Button(self, text="Modificar elemento", command=self.modify_Element)
        btnOrder.pack()

    def modify_Element(self):
        database = FoodElementDAO(connection_string)

        Name_selection = self.selected_Name.get()
        dayMoment_selection = self.selected_dayMoment.get()

        database.updateElement(Name_selection, dayMoment_selection)