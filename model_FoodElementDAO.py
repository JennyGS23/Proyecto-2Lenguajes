import pyodbc
from controller_Main import DatabaseConnection
from model_FoodElement import Calorie, FoodElement, Price

# Establish a connection to the database
connectionString = DatabaseConnection()

# Class FoodElementDAO
class FoodElementDAO:
    def __init__(self, connectionString):
        self.connectionString = connectionString

    def getFoodElements(self):
        # Fetch food elements from the database
        foodElements = []
        cursor = self.connectionString.connection.cursor()
        cursor.execute("SELECT * FROM ElementoComida")
        for row in cursor:
            id, name, type, description, dayMoment = row
            foodElement = FoodElement()
            foodElement.setName(name)
            foodElement.setType(type)
            foodElement.setDescription(description)
            foodElement.setDayMoment(dayMoment)
            foodElements.append(foodElement)
        cursor.close()
        return foodElements

    def getCalories(self):
        # Fetch calorie information from the database
        caloriesList = []
        cursor = self.connectionString.connection.cursor()
        cursor.execute("SELECT ID, Nombre, CantidadCalorias FROM Calorias")
        for row in cursor:
            id, name, calories = row
            calorie = Calorie()
            calorie.setName(name)
            calorie.setCalories(calories)
            caloriesList.append(calorie)
        cursor.close()
        return caloriesList
    
    def getPrices(self):
        # Fetch calorie information from the database
        priceList = []
        cursor = self.connectionString.connection.cursor()
        cursor.execute("SELECT ID, Nombre, Costo FROM Precio")
        for row in cursor:
            id, name, cost = row
            price = Price()
            price.setName(name)
            price.setPrice(cost)
            priceList.append(price)
        cursor.close()
        return priceList


# Create an instance of FoodElementDAO
dao = FoodElementDAO(connectionString)

# Retrieve food elements and calorie information
foodElements = dao.getFoodElements()
calories = dao.getCalories()
prices = dao.getPrices()

# Close the database connection
dao.connectionString.connection.close()

# Write data to a file named 'datos.pl'
with open('datos.pl', 'w') as f:
    # Write data for food elements
    for foodElement in foodElements:
        f.write(f'elementoComida({foodElement.getName()}, {foodElement.getType()}, {foodElement.getDescription()}, {foodElement.getDayMoment()}).\n')
    # Write data for calories
    for calorie in calories:
        f.write(f'calorias({calorie.getName()}, {calorie.getCalories()}).\n')
    # Write data for prices
    for price in prices:
        f.write(f'precio({price.getName()}, {price.getPrice()}).\n')
