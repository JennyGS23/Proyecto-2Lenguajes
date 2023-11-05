import tkinter as tk
from tkinter import ttk
from tkinter import BooleanVar
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

        # RadioButtons para el pago único
        self.uniquePayVar = BooleanVar()
        framePay = tk.Frame(self)
        framePay.pack()
        lblPay = tk.Label(framePay, text="Pago único:")
        lblPay.pack(side="left")
        rbYes = tk.Radiobutton(framePay, text="Sí", variable=self.uniquePayVar, value=True)
        rbNo = tk.Radiobutton(framePay, text="No", variable=self.uniquePayVar, value=False)
        rbYes.pack(side="left")
        rbNo.pack(side="left")

        # Botón calcular
        btnOrder = tk.Button(self, text="Pedir", command=self.Ordenar)
        btnOrder.pack()

    def Ordenar(self):
        selected_seats = int(self.selectedSeats.get())  # Obtener el valor seleccionado y convertirlo a entero
        unique_pay = self.uniquePayVar.get()  # Obtener el valor booleano de los RadioButtons
        self.withdraw()  # Ocultar la ventana actual
        order = OrderView(self, cantClient=selected_seats, uniquePay=unique_pay)
        print(unique_pay)
