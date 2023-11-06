import tkinter as tk
from tkinter import StringVar


class stadisticsView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Estadísticas")
        self.geometry("500x500")

        label = tk.Label(self, text="Estadísticas")
        label.pack()

        # Variables de clase para los valores de Entry
        self.Combo = StringVar()
        self.Parcial = StringVar()
        

        frameCombo = tk.Frame(self)
        frameCombo.pack()
        lblCombo = tk.Label(frameCombo, text="Combo más pedido")
        lblCombo.pack()
        entryCombo = tk.Entry(frameCombo, textvariable=self.Combo, state="readonly")
        entryCombo.pack(side="left")

        frameParcial = tk.Frame(self)
        frameParcial.pack()
        lblParcial = tk.Label(frameParcial, text="Parcial más pedido")
        lblParcial.pack()
        entryParcial = tk.Entry(frameParcial, textvariable=self.Parcial, state="readonly")
        entryParcial.pack(side="left")


    
