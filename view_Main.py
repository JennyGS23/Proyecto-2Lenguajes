import tkinter as tk

class RestaurantView:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Inicio")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Bienvenido al Panel de Inicio")
        self.label.pack()

        # Botón para acceder a la gestión del inventario
        self.inventory_button = tk.Button(root, text="Gestión de Inventario", command=self.open_inventory)
        self.inventory_button.pack()

        # Botón para registrar órdenes de clientes
        self.order_button = tk.Button(root, text="Registrar Órdenes", command=self.open_orders)
        self.order_button.pack()

    def open_inventory(self):
        # Deberías implementar la lógica para abrir la ventana de gestión de inventario aquí.
        print("Abriendo la ventana de gestión de inventario.")

    def open_orders(self):
        # Deberías implementar la lógica para abrir la ventana de registro de órdenes aquí.
        print("Abriendo la ventana de registro de órdenes.")

if __name__ == "__main__":
    root = tk.Tk()

    view = RestaurantView(root)
    
    root.mainloop()
