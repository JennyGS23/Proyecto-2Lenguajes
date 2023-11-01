import tkinter as tk
from tkinter import ttk
from view_Order import OrderView

class TableView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pedir mesa")
        self.geometry("300x200")

        label = tk.Label(self, text="Pide una mesa")
        label.pack()

        # ComboBox cantSeats
        self.selectedSeats = tk.StringVar()  
        frameSeats = tk.Frame(self)
        frameSeats.pack()
        lblSeats = tk.Label(frameSeats, text="Cantidad de asientos:")
        lblSeats.pack(side="left")
        comboSeats = ttk.Combobox(frameSeats, values=["1", "2", "3", "4", "5"], state="readonly", textvariable=self.selectedSeats)
        comboSeats.pack(side="left")

        # ComboBox pay
        self.selectedPay = tk.StringVar()  # Corregir el nombre de la variable
        framePay = tk.Frame(self)
        framePay.pack()
        lblPay = tk.Label(framePay, text="Pago único:")
        lblPay.pack(side="left")
        comboPay = ttk.Combobox(framePay, values=["Sí", "No"], state="readonly", textvariable=self.selectedPay)
        comboPay.pack(side="left")

        # Botón calcular
        btnOrder = tk.Button(self, text="Pedir", command=self.Ordenar)
        btnOrder.pack()

    def Ordenar(self):
        selected_seats = int(self.selectedSeats.get())  # Obtener el valor seleccionado y convertirlo a entero
        self.withdraw()  # Ocultar la ventana actual
        order = OrderView(self, cantClient=selected_seats)
