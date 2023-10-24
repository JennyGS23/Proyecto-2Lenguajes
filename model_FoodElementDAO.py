
# Importa las clases que necesitas
import pyodbc
from controller_Main import DatabaseConnection

from model_FoodElement import FoodElement
#from FoodElement import FoodElement
#from Controller.MainController import DatabaseConnection




# Importa la clase DatabaseConnection
#from Controller.MainController.py import DatabaseConnection

# Define tu conexión a la base de datos
connection_string = DatabaseConnection()

# Clase FoodElementDAO
class FoodElementDAO:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_food_elements(self):
        food_elements = []
        cursor = self.connection_string.connection.cursor()
        cursor.execute("SELECT E.*, C.CantidadCalorias FROM ElementoComida E LEFT JOIN Calorias C ON E.ID = C.ID")
        for row in cursor:
            id, name, type, description, day_moment, calories = row
            food_element = FoodElement(name, type, description, day_moment, calories)
            food_elements.append(food_element)
        cursor.close()
        return food_elements

    


# Crear una instancia de FoodElementDAO
dao = FoodElementDAO(connection_string)

# Obtener la lista de elementos de comida desde la base de datos
food_elements = dao.get_food_elements()

# Cerrar la conexión de la base de datos cuando hayas terminado
dao.connection_string.connection.close()

# Ahora tienes una lista de objetos FoodElement desde la base de datos
for food_element in food_elements:
    print(food_element)




