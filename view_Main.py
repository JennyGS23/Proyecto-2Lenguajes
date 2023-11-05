import tkinter as tk
from view_Changes import ChangesView
from view_Table import TableView

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ventana Principal")
        self.geometry("300x200")
        
        # Botón para abrir la segunda ventana
        btn_abrir_segunda_ventana = tk.Button(self, text="Pedir mesa", command=self.abrir_segunda_ventana)
        btn_abrir_segunda_ventana.pack()

        # Botón para abrir la segunda ventana
        btn_modificaciones = tk.Button(self, text="Realizar modificaciones", command=self.modificaciones_ventana)
        btn_modificaciones.pack()

    def abrir_segunda_ventana(self):
        app = TableView()

    def modificaciones_ventana(self):
        app = ChangesView()