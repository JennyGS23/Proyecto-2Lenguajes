import tkinter as tk
from view_Table import TableView

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ventana Principal")
        self.geometry("300x200")
        
        # Botón para abrir la segunda ventana
        btn_abrir_segunda_ventana = tk.Button(self, text="Pedir mesa", command=self.abrir_segunda_ventana)
        btn_abrir_segunda_ventana.pack()

    def abrir_segunda_ventana(self):
        # Crea una instancia de la segunda ventana
        mesa = TableView(self)