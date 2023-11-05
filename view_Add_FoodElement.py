import tkinter as tk
import tkinter 

class Add_FoodElement_View(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones para Agregar")
        self.geometry("900x500")

        label = tk.Label(self, text="Escoge el menú donde deseas agregar")
        label.pack()

        