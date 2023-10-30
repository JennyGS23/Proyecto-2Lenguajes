class Controlador:

    def __init__(self):
        self.modelo = model_PrologInterpreter()

    def procesar_datos(self, datos):
        resultado = self.modelo.procesar_datos(datos)
        # Puedes realizar más operaciones o enviar el resultado a la vista si es necesario.
        return resultado
