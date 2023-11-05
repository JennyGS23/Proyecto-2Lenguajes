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
    
    def deleteFoodElementByName(self, name):
        # Eliminar un registro por nombre en la tabla ElementoComida
        cursor = self.connectionString.connection.cursor()
        cursor.execute("DELETE FROM ElementoComida WHERE Nombre = ?", (name,))
        self.connectionString.connection.commit()
        cursor.close()

    def deleteCaloriesByName(self, name):
        # Eliminar un registro por nombre en la tabla Calorias
        cursor = self.connectionString.connection.cursor()
        cursor.execute("DELETE FROM Calorias WHERE Nombre = ?", (name,))
        self.connectionString.connection.commit()
        cursor.close()

    def deletePriceByName(self, name):
        # Eliminar un registro por nombre en la tabla Precio
        cursor = self.connectionString.connection.cursor()
        cursor.execute("DELETE FROM Precio WHERE Nombre = ?", (name,))
        self.connectionString.connection.commit()
        cursor.close()


    def AddElement(self, Nombre, Tipo, Descripcion, MomentoDelDia):
        # Add a new meal to the database
        cursor = self.connectionString.connection.cursor()
        #print(drink, protein, sideDish)
        cursor.execute("INSERT INTO ElementoComida (Nombre, Tipo, Descripcion, MomentoDelDia) VALUES ( ?, ?, ?, ?)",
                       (Nombre, Tipo, Descripcion, MomentoDelDia))
        self.connectionString.connection.commit()
        cursor.close()
    
    def AddCalorie(self, Nombre, CantidadCalorias):
        # Add a new meal to the database
        cursor = self.connectionString.connection.cursor()
        #print(drink, protein, sideDish)
        cursor.execute("INSERT INTO Calorias (Nombre, CantidadCalorias) VALUES ( ?, ?)",
                       (Nombre, CantidadCalorias))
        self.connectionString.connection.commit()
        cursor.close()
    
    def AddPrice(self, Nombre, Costo):
        # Add a new meal to the database
        cursor = self.connectionString.connection.cursor()
        #print(drink, protein, sideDish)
        cursor.execute("INSERT INTO Precio (Nombre, Costo) VALUES ( ?, ?)",
                       (Nombre, Costo))
        self.connectionString.connection.commit()
        cursor.close()

    
    def updateElement(self, Nombre, NuevoMomentoDia):
        # Actualiza el precio de un combo de comida en la base de datos
        cursor = self.connectionString.connection.cursor()
        cursor.execute("UPDATE ElementoComida SET MomentoDelDia = ? WHERE Nombre = ? ",
                       (Nombre, NuevoMomentoDia))
        self.connectionString.connection.commit()
        cursor.close()

#*******************************************************************************Importar al main
    def exportDataToPLFile(dao, output_filename):
        dao = FoodElementDAO(connectionString)
        # Retrieve food elements, calorie information, and prices
        foodElements = dao.getFoodElements()
        calories = dao.getCalories()
        prices = dao.getPrices()

        # Write data to the specified PL file
        with open(output_filename, 'w') as f:
            # Write data for food elements
            for foodElement in foodElements:
                f.write(f'elementoComida({foodElement.getName()}, {foodElement.getType()}, {foodElement.getDescription()}, {foodElement.getDayMoment()}).\n')
            # Write data for calories
            for calorie in calories:
                f.write(f'calorias({calorie.getName()}, {calorie.getCalories()}).\n')
            # Write data for prices
            for price in prices:
                f.write(f'precio({price.getName()}, {price.getPrice()}).\n')

        # Close the database connection
        dao.connectionString.connection.close()


# #Create an instance of FoodElementDAO
# dao = FoodElementDAO(connectionString)

# # Retrieve food elements and calorie information
# foodElements = dao.getFoodElements()
# calories = dao.getCalories()
# prices = dao.getPrices()

# # Close the database connection
# dao.connectionString.connection.close()

# # Write data to a file named 'datos.pl'
# with open('datos.pl', 'w') as f:
#     # Write data for food elements
#     for foodElement in foodElements:
#         f.write(f'elementoComida({foodElement.getName()}, {foodElement.getType()}, {foodElement.getDescription()}, {foodElement.getDayMoment()}).\n')
#     # Write data for calories
#     for calorie in calories:
#         f.write(f'calorias({calorie.getName()}, {calorie.getCalories()}).\n')
#     # Write data for prices
#     for price in prices:
#         f.write(f'precio({price.getName()}, {price.getPrice()}).\n')
