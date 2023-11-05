import tkinter as tk
import tkinter
from view_Add_Combo import Add_Combo_View

from view_Add_FoodElement import Add_FoodElement_View
from view_Add_Parcial import Add_Parcial_View 

class AddView(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones para Agregar")
        self.geometry("900x500")

        label = tk.Label(self, text="Escoge el menú donde deseas agregar")
        label.pack()

        # Crear un Frame para los botones de cada cliente
        frame_buttons = tk.Frame(self)
        frame_buttons.pack()

        btnAdd_Element = tk.Button(frame_buttons, text="Elemento comida", command= self.Add_ElementoComida)
        btnAdd_Element.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

        btnAdd_Combo = tk.Button(frame_buttons, text="Combo", command= self.Add_Combo)
        btnAdd_Combo.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

        btnAdd_Parcial = tk.Button(frame_buttons, text="Parcial", command= self.Add_Parcial)
        btnAdd_Parcial.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

    def Add_ElementoComida(self):
        self.withdraw()  # Ocultar la ventana actual
        add_view = Add_FoodElement_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(add_view)  # Espera hasta que se cierre la ventana

    def Add_Combo(self):
        self.withdraw()  # Ocultar la ventana actual
        add_view = Add_Combo_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(add_view)  # Espera hasta que se cierre la ventana
    
    def Add_Parcial(self):
        self.withdraw()  # Ocultar la ventana actual
        add_view = Add_Parcial_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(add_view)  # Espera hasta que se cierre la ventana