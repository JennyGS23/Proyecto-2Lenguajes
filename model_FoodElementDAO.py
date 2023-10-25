
# Importa las clases que necesitas
import pyodbc
from controller_Main import DatabaseConnection

from model_FoodElement import Calorie, FoodElement


# Define tu conexión a la base de datos
connection_string = DatabaseConnection()

# Clase FoodElementDAO
class FoodElementDAO:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    # def get_food_elements(self):
    #     food_elements = []
    #     cursor = self.connection_string.connection.cursor()
    #     cursor.execute("SELECT E.*, C.CantidadCalorias FROM ElementoComida E LEFT JOIN Calorias C ON E.ID = C.ID")
    #     for row in cursor:
    #         id, name, type, description, day_moment, calories = row
    #         food_element = FoodElement(name, type, description, day_moment, calories)
    #         food_elements.append(food_element)
    #     cursor.close()
    #     return food_elements
    def get_food_elements(self):
        food_elements = []
        cursor = self.connection_string.connection.cursor()
        cursor.execute("SELECT * FROM ElementoComida")
        for row in cursor:
            id, name, type, description, day_moment = row
            food_element = FoodElement(name, type, description, day_moment)
            food_elements.append(food_element)
        cursor.close()
        return food_elements
    
   
    def get_calories(self):
        caloriesList = []
        cursor = self.connection_string.connection.cursor()
        cursor.execute("SELECT ID, Nombre, CantidadCalorias FROM Calorias")
        for row in cursor:
            id, name, calories = row
            calorie = Calorie(name, calories)
            caloriesList.append(calorie)
        cursor.close()
        return caloriesList

  


# Crear una instancia de FoodElementDAO
dao = FoodElementDAO(connection_string)

# Obtener la lista de elementos de comida desde la base de datos
food_elements = dao.get_food_elements()
calories = dao.get_calories()

# Cerrar la conexión de la base de datos cuando hayas terminado
dao.connection_string.connection.close()

#Ahora tienes una lista de objetos FoodElement desde la base de datos
with open('datos.pl', 'w') as f:
    for food_element in food_elements:
        print(food_element)
    for calorie in calories:
        print(calorie)


with open('datos.pl', 'w') as f:
    # Write data for food elements
    for food_element in food_elements:
        f.write(f'elementoComida({food_element.name}, {food_element.type}, {food_element.description}, {food_element.dayMoment}).\n')
    # Write data for calories
    for calorie in calories:
        f.write(f'calorias({calorie.name}, {calorie.calories}).\n')

    
    





