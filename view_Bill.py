import tkinter as tk
from tkinter import StringVar
from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Factura', align='C', ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

def create_pdf(id, date, client, order, price):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'ID: {id}', ln=True)
    pdf.cell(0, 10, f'Fecha: {date}', ln=True)
    pdf.cell(0, 10, f'Cliente: {client}', ln=True)
    pdf.cell(0, 10, f'Orden realizada: {order}', ln=True)
    pdf.cell(0, 10, f'Precio: ${price}', ln=True)
    filename = f'factura{id}.pdf'
    pdf.output(filename)

class BillView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Factura")
        self.geometry("500x500")

        label = tk.Label(self, text="Factura")
        label.pack()

        # Variables de clase para los valores de Entry
        self.id_var = StringVar()
        self.date_var = StringVar()
        self.client_var = StringVar()
        self.order_var = StringVar()
        self.price_var = StringVar()

        frameID = tk.Frame(self)
        frameID.pack()
        lblID = tk.Label(frameID, text="ID")
        lblID.pack()
        entryID = tk.Entry(frameID, textvariable=self.id_var, state="readonly")
        entryID.pack(side="left")

        frameDate = tk.Frame(self)
        frameDate.pack()
        lblDate = tk.Label(frameDate, text="Fecha")
        lblDate.pack()
        entryDate = tk.Entry(frameDate, textvariable=self.date_var, state="readonly")
        entryDate.pack(side="left")

        frameClient = tk.Frame(self)
        frameClient.pack()
        lblClient = tk.Label(frameClient, text="Cliente")
        lblClient.pack()
        entryClient = tk.Entry(frameClient, textvariable=self.client_var, state="readonly")
        entryClient.pack(side="left")

        frameOrder = tk.Frame(self)
        frameOrder.pack()
        lblOrder = tk.Label(frameOrder, text="Orden realizada")
        lblOrder.pack()
        entryOrder = tk.Entry(frameOrder, textvariable=self.order_var, state="readonly")
        entryOrder.pack(side="left")

        framePrice = tk.Frame(self)
        framePrice.pack()
        lblPrice = tk.Label(framePrice, text="Precio")
        lblPrice.pack()
        entryPrice = tk.Entry(framePrice, textvariable=self.price_var, state="readonly")
        entryPrice.pack(side="left")

        # Botón pagar
        btnPagar = tk.Button(self, text="Pagar", command=self.Pagar)
        btnPagar.pack()

    def Pagar(self):
        # Obtén los valores de las variables de clase
        id = self.id_var.get()
        current_date = datetime.now().strftime('%Y-%m-%d')
        client = self.client_var.get()
        order = self.order_var.get()
        price = self.price_var.get()

        # Asigna la fecha actual a la variable date_var
        self.date_var.set(current_date)

        # Crea el PDF con los datos de la factura
        create_pdf(id, current_date, client, order, price)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = BillView(master=root)
#     app.id_var.set("12345")
#     # La fecha se establecerá automáticamente en la función Pagar
#     app.client_var.set("Cliente Ejemplo")
#     app.order_var.set("Orden de Prueba")
#     app.price_var.set("100.00")
#     app.mainloop()
