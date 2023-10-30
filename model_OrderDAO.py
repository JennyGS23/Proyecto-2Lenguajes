import pyodbc
from controller_Main import DatabaseConnection
from model_MealCombo import ComboMeal
from model_Order import Order

# Establish a connection to the database
connection_string = DatabaseConnection()

# Class MealDAO
class ComboMealDAO:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def getMeal(self):
        # Fetch meals from the database
        orders = []
        cursor = self.connection_string.connection.cursor()
        cursor.execute("SELECT * FROM Orders")
        for row in cursor:
            id, drink, meal, price= row
            order = Order()
            order.setId(id)
            order.setMeal(meal)
            order.setPrice(price)
            orders.append(order)
        cursor.close()
        return orders
    
    def setMeal(self, meal, price):
        # Add a new meal to the database
        cursor = self.connection_string.connection.cursor()
        cursor.execute("INSERT INTO Orders (meal, price) VALUES (?, ?, ?)",
                       (meal, price))
        self.connection_string.connection.commit()
        cursor.close()

# Create an instance of FoodElementDAO
#dao = MealDAO(connection_string)

# Retrieve food elements and calorie information
#meals = dao.getMeal()

#dao.setMeal(new_drink, new_protein, new_sideDish, new_dessert, new_dayMoment, new_minCalories)

# Close the database connection
#dao.connection_string.connection.close()