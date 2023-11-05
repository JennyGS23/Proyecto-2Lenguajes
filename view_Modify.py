import tkinter as tk
import tkinter

from view_Modify_Combo import Modify_Combo_View
from view_Modify_FoodElement import Modify_FoodElement_View
from view_Modify_Parcial import Modify_Parcial_View 


class ModifyView(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones para Modificar")
        self.geometry("900x500")

        label = tk.Label(self, text="Escoge el menú donde deseas modificar")
        label.pack()

        # Crear un Frame para los botones de cada cliente
        frame_buttons = tk.Frame(self)
        frame_buttons.pack()

        btnModify_Element = tk.Button(frame_buttons, text="Elemento comida", command= self.Modify_ElementoComida)
        btnModify_Element.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

        btnModify_Combo = tk.Button(frame_buttons, text="Combo", command= self.Modify_Combo)
        btnModify_Combo.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

        btnModify_Parcial = tk.Button(frame_buttons, text="Parcial", command= self.Modify_Parcial)
        btnModify_Parcial.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

    def Modify_ElementoComida(self):
        self.withdraw()  # Ocultar la ventana actual
        modify_view = Modify_FoodElement_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(modify_view)  # Espera hasta que se cierre la ventana

    def Modify_Combo(self):
        self.withdraw()  # Ocultar la ventana actual
        modify_view = Modify_Combo_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(modify_view)  # Espera hasta que se cierre la ventana
    
    def Modify_Parcial(self):
        self.withdraw()  # Ocultar la ventana actual
        modify_view = Modify_Parcial_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(modify_view)  # Espera hasta que se cierre la ventana