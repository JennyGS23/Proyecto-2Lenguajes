import tkinter as tk
from view_MealCombo import ComboMealView
from view_MealHealthy import HealthyMealView
from view_MealParcial import ParcialMealView

class OrderView(tk.Toplevel):
    def __init__(self, master=None, cantClient=None, uniquePay=None):
        super().__init__(master)
        self.cantClient = cantClient
        self.uniquePay = uniquePay
        self.title("Ordena")
        self.geometry("1000x500")

        label = tk.Label(self, text="Realice las órdenes")
        label.pack()

        if self.uniquePay:
            label = tk.Label(self, text="Realice las órdenes")
            label.pack()

        # Un diccionario para mantener un seguimiento de los Listbox de cada cliente
        self.listboxes = {}

        for client_number in range(1, self.cantClient + 1):
            lblCliente = tk.Label(self, text=f"Cliente número {client_number}:")
            lblCliente.pack()

            # Crear un Frame para los botones de cada cliente
            frame_buttons = tk.Frame(self)
            frame_buttons.pack()

            btnCombo = tk.Button(frame_buttons, text="Ordenar combo", command=lambda client=client_number: self.ordenar_combo(client))
            btnCombo.pack(side=tk.LEFT, padx=5)

            btnParcial = tk.Button(frame_buttons, text="Ordenar parcial", command=lambda client=client_number: self.ordenar_parcial(client))
            btnParcial.pack(side=tk.LEFT, padx=5)

            btnHealthy = tk.Button(frame_buttons, text="Ordenar saludable", command=lambda client=client_number: self.ordenar_saludable(client))
            btnHealthy.pack(side=tk.LEFT, padx=5)

            # Listbox para mostrar los resultados
            frame_listbox = tk.Frame(self)
            frame_listbox.pack()
            listbox = tk.Listbox(frame_listbox, width=200, height=2)
            listbox.pack()

            # Agregar el Listbox al diccionario con el número de cliente como clave
            self.listboxes[client_number] = listbox

            if not self.uniquePay:
                    btnPagar = tk.Button(frame_buttons, text=f"Pagar Cliente {client_number}", command=lambda client=client_number: self.pagar(client=client_number))
                    btnPagar.pack(side=tk.LEFT, padx=5)
            
        if self.uniquePay:
            btnPagar = tk.Button(self, text="Pagar", command=None)
            btnPagar.pack(side=tk.BOTTOM, padx=5)

    def ordenar_combo(self, client_number):
        # Lógica para ordenar un combo para el cliente 'client_number'
        print(f"Ordenar combo para el cliente {client_number}")
        combo_meal_view = ComboMealView(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(combo_meal_view)  # Espera hasta que se cierre la ventana
       
        selected_option = combo_meal_view.selected_option.get()

        # Muestra la selección en el Listbox del cliente correspondiente
        listbox = self.listboxes.get(client_number)
        if listbox:
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, f"Selección de comida saludable para el cliente {client_number}: {selected_option}")

    def ordenar_parcial(self, client_number):
        # Lógica para ordenar un combo para el cliente 'client_number'
        print(f"Ordenar comida Parcial para el cliente {client_number}")
        parcial_meal_view = ParcialMealView(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(parcial_meal_view)  # Espera hasta que se cierre la ventana
       
        selected_option = parcial_meal_view.selected_option.get()

        # Muestra la selección en el Listbox del cliente correspondiente
        listbox = self.listboxes.get(client_number)
        if listbox:
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, f"Selección de comida saludable para el cliente {client_number}: {selected_option}")

    def ordenar_saludable(self, client_number):
        return
        # Lógica para ordenar una comida saludable para el cliente 'client_number'
        print(f"Ordenar comida saludable para el cliente {client_number}")
        #orden = HealthyMealView()

        healthy_meal_view = HealthyMealView(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(healthy_meal_view)  # Espera hasta que se cierre la ventana

        # Accede a la selección almacenada en la ventana HealthyMealView
        selected_option = healthy_meal_view.selected_option.get()
 
         # Muestra la selección en el Listbox del cliente correspondiente
        listbox = self.listboxes.get(client_number)
        if listbox:
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, f"Selección de comida saludable para el cliente {client_number}: {selected_option}")

        
