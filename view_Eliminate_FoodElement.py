import tkinter as tk
import tkinter 

class Eliminate_FoodElement_View(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones para Elimiar")
        self.geometry("900x500")

        label = tk.Label(self, text="Escoge el menú donde deseas eliminar")
        label.pack()