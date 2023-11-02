import tkinter as tk
from view_MealHealthy import HealthyMealView

class OrderView(tk.Toplevel):
    def __init__(self, master=None, cantClient=None):
        super().__init__(master)
        self.cantClient = cantClient 
        self.title("Ordena")
        self.geometry("600x600")

        label = tk.Label(self, text="Realice las órdenes")
        label.pack()

        for client_number in range(1, self.cantClient + 1):
            lblCliente = tk.Label(self, text=f"Cliente número {client_number}:")
            lblCliente.pack()

            # Crear un Frame para los botones de cada cliente
            frame_buttons = tk.Frame(self)
            frame_buttons.pack()

            btnCombo = tk.Button(frame_buttons, text="Ordenar combo", command=lambda client=client_number: self.ordenar_combo(client))
            btnCombo.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

            btnParcial = tk.Button(frame_buttons, text="Ordenar parcial", command=lambda client=client_number: self.ordenar_parcial(client))
            btnParcial.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

            btnHealthy = tk.Button(frame_buttons, text="Ordenar saludable", command=lambda client=client_number: self.ordenar_saludable(client))
            btnHealthy.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

            # Listbox para mostrar los resultados
            frame_listbox = tk.Frame(self)
            frame_listbox.pack()
            self.listbox = tk.Listbox(frame_listbox, width=40, height=1)
            self.listbox.pack()

        btnPagar = tk.Button(frame_buttons, text="Pagar", command=lambda client=client_number: self.ordenar_saludable(client))
        btnPagar.pack(side=tk.LEFT, padx=5)  # Alinea a la izquierda con un espacio de 5 píxeles

    def ordenar_combo(self, client_number):
        # Lógica para ordenar un combo para el cliente 'client_number'
        print(f"Ordenar combo para el cliente {client_number}")

    def ordenar_parcial(self, client_number):
        # Lógica para ordenar un menú parcial para el cliente 'client_number'
        print(f"Ordenar menú parcial para el cliente {client_number}")

    def ordenar_saludable(self, client_number):
        # Lógica para ordenar una comida saludable para el cliente 'client_number'
        print(f"Ordenar comida saludable para el cliente {client_number}")
        orden = HealthyMealView()
