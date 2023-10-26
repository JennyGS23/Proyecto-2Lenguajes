import pyodbc
from controller_Main import DatabaseConnection
from model_FoodElement import Calorie, FoodElement

# Establish a connection to the database
connection_string = DatabaseConnection()

# Class FoodElementDAO
class FoodElementDAO:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_food_elements(self):
        # Fetch food elements from the database
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
        # Fetch calorie information from the database
        caloriesList = []
        cursor = self.connection_string.connection.cursor()
        cursor.execute("SELECT ID, Nombre, CantidadCalorias FROM Calorias")
        for row in cursor:
            id, name, calories = row
            calorie = Calorie(name, calories)
            caloriesList.append(calorie)
        cursor.close()
        return caloriesList

# Create an instance of FoodElementDAO
dao = FoodElementDAO(connection_string)

# Retrieve food elements and calorie information
food_elements = dao.get_food_elements()
calories = dao.get_calories()

# Close the database connection
dao.connection_string.connection.close()

# Write data to a file named 'datos.pl'
with open('datos.pl', 'w') as f:
    # Write data for food elements
    for food_element in food_elements:
        f.write(f'elementoComida({food_element.name}, {food_element.type}, {food_element.description}, {food_element.dayMoment}).\n')
    # Write data for calories
    for calorie in calories:
        f.write(f'calorias({calorie.name}, {calorie.calories}).\n')
