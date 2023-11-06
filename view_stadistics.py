import tkinter as tk
from tkinter import StringVar
from functools import reduce

class stadisticsView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Estadísticas")
        self.geometry("600x500")

        label = tk.Label(self, text="Estadísticas")
        label.pack()

        # Variables de clase para los valores de Entry
        self.Combo = StringVar()
        self.Parcial = StringVar()
        self.Combo.set("")

        frameCombo = tk.Frame(self)
        frameCombo.pack()
        lblCombo = tk.Label(frameCombo, text="Combo más pedido")
        lblCombo.pack()
        entryCombo = tk.Entry(frameCombo, textvariable=self.Combo, state="readonly", width=500)
        entryCombo.pack(side="left")

        # Botón para abrir la segunda ventana
        btn_modificaciones = tk.Button(self, text="Mostrar", command=self.count_id_occurrences_combo)
        btn_modificaciones.pack()

        frameParcial = tk.Frame(self)
        frameParcial.pack()
        lblParcial = tk.Label(frameParcial, text="Parcial más pedido")
        lblParcial.pack()
        entryParcial = tk.Entry(frameParcial, textvariable=self.Parcial, state="readonly",width=500)
        entryParcial.pack(side="left")

        # Botón para abrir la segunda ventana
        btn_modificaciones2 = tk.Button(self, text="Mostrar", command=self.count_id_occurrences_Parcial)
        btn_modificaciones2.pack()

    def count_id_occurrences_combo(self):
        # Leer el archivo txt y realizar el procesamiento
        with open("seleccionCombo.txt", "r") as file:
            lines = file.readlines()

        # Función para contar la ocurrencia de cada ID
        def count_id_occurrences_inner(id_count, line):
            parts = line.split(',')
            id = int(parts[0].split(':')[1])
            id_count[id] = id_count.get(id, 0) + 1
            return id_count

        id_counts = reduce(count_id_occurrences_inner, lines, {})

        # Encontrar el ID más repetido
        most_common_id = max(id_counts, key=id_counts.get)

        # Filtrar las líneas correspondientes al ID más repetido
        most_common_lines = list(filter(lambda line: int(line.split(',')[0].split(':')[1]) == most_common_id, lines))

        # Establecer el valor en entryCombo
        self.Combo.set('\n'.join(most_common_lines))


        
    def count_id_occurrences_Parcial(self):
        # Leer el archivo txt y realizar el procesamiento
        with open("seleccionParcial.txt", "r") as file:
            lines = file.readlines()

        # Función para contar la ocurrencia de cada ID
        def count_id_occurrences_inner(id_count, line):
            parts = line.split(',')
            id = int(parts[0].split(':')[1])
            id_count[id] = id_count.get(id, 0) + 1
            return id_count

        id_counts = reduce(count_id_occurrences_inner, lines, {})

        # Encontrar el ID más repetido
        most_common_id = max(id_counts, key=id_counts.get)

        # Filtrar las líneas correspondientes al ID más repetido
        most_common_lines = list(filter(lambda line: int(line.split(',')[0].split(':')[1]) == most_common_id, lines))

        # Establecer el valor en entryCombo
        self.Parcial.set('\n'.join(most_common_lines))

if __name__ == "__main__":
    root = tk.Tk()
    app = stadisticsView(root)
    root.mainloop()
