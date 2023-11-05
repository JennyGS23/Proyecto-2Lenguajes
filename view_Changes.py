import tkinter as tk
from view_Add import AddView
from view_Eliminate import EliminateView

from view_Modify import ModifyView
    
class ChangesView(tk.Toplevel):
    
    def __init__(self, master=None, cantClient=None):
        super().__init__(master)
        self.cantClient = cantClient 
        self.title("Modifica")
        self.geometry("1000x500")

        label = tk.Label(self, text="Realice las modificaciones")
        label.pack()

     
        # Crear un Frame para los botones de cada cliente
        frame_buttons = tk.Frame(self)
        frame_buttons.pack()

        btnAdd = tk.Button(frame_buttons, text="Agregar", command= self.Add)
        btnAdd.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

        btnEliminate = tk.Button(frame_buttons, text="Eliminar", command= self.Eliminate)
        btnEliminate.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

        btnModify = tk.Button(frame_buttons, text="Modificar", command= self.Modify)
        btnModify.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

    def Add(self):
        self.withdraw()  # Ocultar la ventana actual
        add_view = AddView(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(add_view)  # Espera hasta que se cierre la ventana

    def Eliminate(self):
        self.withdraw()  # Ocultar la ventana actual
        eliminate_view = EliminateView(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(eliminate_view)  # Espera hasta que se cierre la ventana
    
    def Modify(self):
        self.withdraw()  # Ocultar la ventana actual
        modify_view = ModifyView(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(modify_view)  # Espera hasta que se cierre la ventana