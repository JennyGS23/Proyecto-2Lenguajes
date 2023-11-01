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
        self.selected_seats = tk.StringVar() 
        frame_seats = tk.Frame(self)
        frame_seats.pack()
        lblSeats = tk.Label(frame_seats, text="Cantidad de asientos:")
        lblSeats.pack(side="left")
        comboSeats = ttk.Combobox(frame_seats, values=["1", "2", "3", "4", "5"], state="readonly", textvariable=self.selected_drink)
        comboSeats.pack(side="left")

        # ComboBox selected pay
        self.selected_pay = tk.StringVar() 
        frame_pay = tk.Frame(self)
        frame_pay.pack()
        lblPay = tk.Label(frame_pay, text="Pago unico:")
        lblPay.pack(side="left")
        comboPay = ttk.Combobox(frame_pay, values=["Sí", "No"], state="readonly", textvariable=self.selected_protein)
        comboPay.pack(side="left")

        # Botón calcular
        btnTable = tk.Button(self, text="Pedir", command=self.PedirMesa)
        btnTable.pack()

    def PedirMesa(self):
        meal = HealthyMealView()