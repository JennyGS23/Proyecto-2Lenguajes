import tkinter as tk
import tkinter
from tkinter import ttk
from controller_Main import DatabaseConnection

from model_FoodElementDAO import FoodElementDAO 

# Establish a connection to the database
connection_string = DatabaseConnection()
class Add_FoodElement_View(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Agregar Elementos Comida")
        self.geometry("900x500")

        label = tk.Label(self, text="Ingresa los elementos para agregar")
        label.pack()


        self.selected_Name = tk.StringVar()  # Variable para almacenar la selección
        frame_proteins = tk.Frame(self)
        frame_proteins.pack()
        lblProteins = tk.Label(frame_proteins, text="Nombre:")
        lblProteins.pack(side="left")
        comboProteins = tk.Entry(frame_proteins, textvariable=self.selected_Name)
        comboProteins.pack(side="left")

        self.selected_Type = tk.StringVar()  # Variable para almacenar la selección
        frameSeats = tk.Frame(self)
        frameSeats.pack()
        lblSeats = tk.Label(frameSeats, text="Tipo:")
        lblSeats.pack(side="left")
        comboSeats = ttk.Combobox(frameSeats, values=["bebida", "proteina", "acompanamiento", "postre"], state="readonly", textvariable=self.selected_Type)
        comboSeats.pack(side="left")

        self.selected_Description = tk.StringVar()  # Variable para almacenar la selección
        frameSeats = tk.Frame(self)
        frameSeats.pack()
        lblSeats = tk.Label(frameSeats, text="Descripción:")
        lblSeats.pack(side="left")
        comboSeats = ttk.Combobox(frameSeats, values=["natural", "carbonatada", "caliente", "con_lacteo"], state="readonly", textvariable=self.selected_Description)
        comboSeats.pack(side="left")


        # ComboBox Time
        self.selected_Time = tk.StringVar()  
        frameSeats = tk.Frame(self)
        frameSeats.pack()
        lblSeats = tk.Label(frameSeats, text="Momento del dia:")
        lblSeats.pack(side="left")
        comboSeats = ttk.Combobox(frameSeats, values=["desayuno", "almuerzo", "cena", "general"], state="readonly", textvariable=self.selected_Time)
        comboSeats.pack(side="left")

        self.selected_Calories = tk.StringVar()  # Variable para almacenar la selección
        frame_price = tk.Frame(self)
        frame_price.pack()
        lblPrice = tk.Label(frame_price, text="Cantidad de calorias: ")
        lblPrice.pack(side="left")
        comboPrice = tk.Entry(frame_price, textvariable=self.selected_Calories)
        comboPrice.pack(side="left")

        self.selected_Price = tk.StringVar()  # Variable para almacenar la selección
        frame_price = tk.Frame(self)
        frame_price.pack()
        lblPrice = tk.Label(frame_price, text="Precio: ")
        lblPrice.pack(side="left")
        comboPrice = tk.Entry(frame_price, textvariable=self.selected_Price)
        comboPrice.pack(side="left")

        # Botón ordenar
        btnNewElement = tk.Button(self, text="Guardar nuevo elemento de comida", command= self.save_New_Element)
        btnNewElement.pack()
    

    def save_New_Element(self,):
        database = FoodElementDAO(connection_string)
        Name_selection = self.selected_Name.get()
        Type_selection = self.selected_Type.get()
        descriptionSelection = self.selected_Description.get()
        dayMomment_selection = self.selected_Time.get()
        calories_selection = self.selected_Calories.get()
        price_selection = self.selected_Price.get()
        
        database.AddElement(Name_selection, Type_selection, descriptionSelection, dayMomment_selection)
        database.AddCalorie(Name_selection, calories_selection)
        database.AddPrice(Name_selection, price_selection)