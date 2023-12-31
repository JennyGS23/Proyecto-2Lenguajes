import tkinter as tk
from tkinter import StringVar, IntVar
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

def create_pdf(id, date, client, order, payment_option):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'ID: {id}', ln=True)
    pdf.cell(0, 10, f'Fecha: {date}', ln=True)
    pdf.cell(0, 10, f'Cliente: {client}', ln=True)
    
    # Dividir el texto de la orden en líneas más cortas
    lines = order.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)  # Utiliza multi_cell para permitir saltos de línea

    payment_option_text = "Pago: Efectivo" if payment_option == 1 else "Pago: Tarjeta"
    pdf.cell(0, 10, payment_option_text, ln=True)  # Agrega la opción de pago al PDF
    
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
        self.payment_option = IntVar(value=1)  # Por defecto, se selecciona Efectivo

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

        # Radio buttons para la opción de pago
        payment_frame = tk.Frame(self)
        payment_frame.pack()
        payment_label = tk.Label(payment_frame, text="Opción de Pago:")
        payment_label.pack()
        efectivo_radio = tk.Radiobutton(payment_frame, text="Efectivo", variable=self.payment_option, value=1)
        efectivo_radio.pack()
        tarjeta_radio = tk.Radiobutton(payment_frame, text="Tarjeta", variable=self.payment_option, value=2)
        tarjeta_radio.pack()

        # Botón pagar
        btnPagar = tk.Button(self, text="Pagar", command=self.Pagar)
        btnPagar.pack()

    def Pagar(self):
        # Obtén los valores de las variables de clase
        id = self.id_var.get()
        current_date = datetime.now().strftime('%Y-%m-%d')
        client = self.client_var.get()
        order = self.order_var.get()
        payment_option = self.payment_option.get()

        # Asigna la fecha actual a la variable date_var
        self.date_var.set(current_date)

        # Crea el PDF con los datos de la factura y la opción de pago
        create_pdf(id, current_date, client, order, payment_option)

if __name__ == "__main__":
    root = tk.Tk()
    app = BillView(master=root)
    app.id_var.set("12345")
    # La fecha se establecerá automáticamente en la función Pagar
    app.client_var.set("Cliente Ejemplo")
    app.order_var.set("Orden de Prueba")
    app.mainloop()
