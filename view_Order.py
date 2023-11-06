import tkinter as tk
import random
from view_Bill import BillView
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
                btnPagar = tk.Button(frame_buttons, text=f"Pagar Cliente {client_number}", command=lambda client=client_number: self.pagar(client))
                btnPagar.pack(side=tk.LEFT, padx=5)
            
        if self.uniquePay:
            btnPagar = tk.Button(self, text="Pagar Cliente Mesa", command= lambda client=client_number: self.pagarUnico(client))
            btnPagar.pack(side=tk.BOTTOM, padx=5)

    def pagar(self, client_number):
        # Genera un número aleatorio largo como ID
        id = random.randrange(100000000000, 999999999999)
        client = f"Cliente {client_number}"  # Reemplaza con el nombre o identificación del cliente
        order = self.listboxes[client_number].get(0)  # Obtén la orden del Listbox del cliente
        price = "200"  # Reemplaza con la lógica para calcular el precio

        # Crea una instancia de BillView y pasa los parámetros necesarios
        bill_view = BillView(self)
        bill_view.id_var.set(id)
        bill_view.client_var.set(client)
        bill_view.order_var.set(order)

        # Muestra la ventana de factura
        self.wait_window(bill_view)


    def pagarUnico(self, client_number):
        
        # Genera un número aleatorio largo como ID
        id = random.randrange(100000000000, 999999999999)
        client = f"Cliente {client_number}"  # Reemplaza con el nombre o identificación del cliente

        # Obtén las órdenes de todos los Listbox y únelas con saltos de línea
        orders = [self.listboxes[i].get(0) if i in self.listboxes else "" for i in range(1, self.cantClient + 1)]
        order = "\n".join(orders)  # Concatena las órdenes con saltos de línea

        #price = "200"  # Reemplaza con la lógica para calcular el precio

        # Crea una instancia de BillView y pasa los parámetros necesarios
        bill_view = BillView(self)
        bill_view.id_var.set(id)
        bill_view.client_var.set(client)
        bill_view.order_var.set(order)

        # Muestra la ventana de factura
        self.wait_window(bill_view)




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
            listbox.insert(tk.END, f"Cliente {client_number}: {selected_option}")

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
            listbox.insert(tk.END, f"Cliente {client_number}: {selected_option}")

    def ordenar_saludable(self, client_number):
        
        # Lógica para ordenar una comida saludable para el cliente 'client_number'
        
        healthy_meal_view = HealthyMealView(self)  # Pasa self como maestro para la nueva ventana
        self.wait_window(healthy_meal_view)  # Espera hasta que se cierre la ventana

        # Accede a la selección almacenada en la ventana HealthyMealView
        selected_option = healthy_meal_view.selected_option.get()
 
         # Muestra la selección en el Listbox del cliente correspondiente
        listbox = self.listboxes.get(client_number)
        if listbox:
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, f"Cliente {client_number}: {selected_option}")

        
