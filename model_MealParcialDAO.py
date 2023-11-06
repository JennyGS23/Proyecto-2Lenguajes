import pyodbc
from controller_Main import DatabaseConnection
from model_MealParcial import ParcialMeal

# Establish a connection to the database
connection_string = DatabaseConnection()

# Class MealDAO
class ParcialMealDAO:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def getMeal(self):
        # Fetch meals from the database
        meals = []
        cursor = self.connection_string.connection.cursor()
        cursor.execute("SELECT * FROM ParcialMeals")
        for row in cursor:
            id, protein, sideDish, price, calorie= row
            meal = ParcialMeal()
            meal.setId(id)
            meal.setProtein(protein)
            meal.setSideDish(sideDish)
            meal.setPrice(price)
            meal.setCalorie(calorie)
            meals.append(meal)
        cursor.close()
        return meals


    def setMeal(self, proteins, sideDish, price, calorie):
        # Add a new meal to the database
        cursor = self.connection_string.connection.cursor()
        cursor.execute("INSERT INTO ParcialMeals(proteins, sideDish, price, calorie) VALUES (?, ?, ?)",
                       (proteins, sideDish, price, calorie))
        self.connection_string.connection.commit()
        cursor.close()


    def deleteMeal(self, proteins, sideDish, price, calorie):
        cursor = self.connection_string.connection.cursor()
        cursor.execute("DELETE FROM ParcialMeals WHERE Proteins = ? AND SideDish = ? AND Price = ? AND Calorie = ?",
                    (proteins, sideDish, price, calorie))
        self.connection_string.connection.commit()
        cursor.close()


    def updatePrice(self, proteins, sideDish, new_price, calorie):
        # Actualiza el precio de un combo de comida en la base de datos
        cursor = self.connection_string.connection.cursor()
        cursor.execute("UPDATE ParcialMeals SET Price = ? WHERE Proteins = ? AND SideDish = ? AND Calorie = ? ",
                       (new_price, proteins, sideDish, calorie))
        self.connection_string.connection.commit()
        cursor.close()