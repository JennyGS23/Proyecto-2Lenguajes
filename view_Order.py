import tkinter as tk
from tkinter import ttk

class OrderView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Órdenes")
        self.geometry("500x500")

        label = tk.Label(self, text="Ordene aquí")
        label.pack()

        # ComboBox para seleccionar tipo de comida
        food_type_label = tk.Label(self, text="Tipo de Comida:")
        food_type_label.pack()
        food_type_combo = ttk.Combobox(self, values=["Pizza", "Hamburguesa", "Ensalada"], state="readonly")
        food_type_combo.pack()

        # ComboBox para seleccionar tamaño de la comida
        size_label = tk.Label(self, text="Tamaño:")
        size_label.pack()
        size_combo = ttk.Combobox(self, values=["Pequeño", "Mediano", "Grande"], state="readonly")
        size_combo.pack()

        # ComboBox para seleccionar extras
        extras_label = tk.Label(self, text="Extras:")
        extras_label.pack()
        extras_combo = ttk.Combobox(self, values=["Papas fritas", "Refresco", "Salsa"], state="readonly")
        extras_combo.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderView(master=root)
    app.mainloop()
