import tkinter as tk
import tkinter
from view_Eliminate_Combo import Eliminate_Combo_View

from view_Eliminate_FoodElement import Eliminate_FoodElement_View
from view_Elminate_Parcial import Eliminate_Parcial_View 

class EliminateView(tkinter.Toplevel):

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Opciones para Eliminar")
        self.geometry("900x500")

        label = tk.Label(self, text="Escoge el menú donde deseas eliminar")
        label.pack()

        # Crear un Frame para los botones de cada cliente
        frame_buttons = tk.Frame(self)
        frame_buttons.pack()

        btnEliminate_Element = tk.Button(frame_buttons, text="Elemento comida", command= self.Eliminate_ElementoComida)
        btnEliminate_Element.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

        btnEliminate_Combo = tk.Button(frame_buttons, text="Combo", command= self.Eliminate_Combo)
        btnEliminate_Combo.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

        btnEliminate_Parcial = tk.Button(frame_buttons, text="Parcial", command= self.Eliminate_Parcial)
        btnEliminate_Parcial.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

    def Eliminate_ElementoComida(self):
        self.withdraw()  # Ocultar la ventana actual
        eliminate_view = Eliminate_FoodElement_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(eliminate_view)  # Espera hasta que se cierre la ventana

    def Eliminate_Combo(self):
        self.withdraw()  # Ocultar la ventana actual
        eliminate_view = Eliminate_Combo_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(eliminate_view)  # Espera hasta que se cierre la ventana
    
    def Eliminate_Parcial(self):
        self.withdraw()  # Ocultar la ventana actual
        eliminate_view = Eliminate_Parcial_View(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(eliminate_view)  # Espera hasta que se cierre la ventana