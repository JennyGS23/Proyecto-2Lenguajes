import pyodbc
from controller_Main import DatabaseConnection
from model_MealCombo import ComboMeal

# Establish a connection to the database
connection_string = DatabaseConnection()

# Class MealDAO
class ComboMealDAO:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def getMeal(self):
        # Fetch meals from the database
        meals = []
        cursor = self.connection_string.connection.cursor()
        cursor.execute("SELECT * FROM ComboMeals")
        for row in cursor:
            id, drink, protein, sideDish, dessert, price, calorie= row
            meal = ComboMeal()
            meal.setId(id)
            meal.setDrink(drink)
            meal.setProtein(protein)
            meal.setSideDish(sideDish)
            meal.setDessert(dessert)
            meal.setPrice(price)
            meal.setCalories(calorie)
            meals.append(meal)
        cursor.close()
        return meals
    
    def setMeal(self, drink, proteins, sideDish, dessert, price, calorie):
        # Add a new meal to the database
        cursor = self.connection_string.connection.cursor()
        #print(drink, protein, sideDish)
        cursor.execute("INSERT INTO ComboMeals (drink, proteins, sideDish, dessert, price, calorie) VALUES ( ?, ?, ?, ?, ?)",
                       (drink, proteins, sideDish, dessert, price, calorie))
        self.connection_string.connection.commit()
        cursor.close()

    def deleteMeal(self, drink, proteins, sideDish, dessert, price, calorie):
        cursor = self.connection_string.connection.cursor()
        cursor.execute("DELETE FROM ComboMeals WHERE Drink = ? AND Proteins = ? AND SideDish = ? AND Dessert = ? AND Price = ? AND Calorie = ?",
                    (drink, proteins, sideDish, dessert, price, calorie))
        self.connection_string.connection.commit()
        cursor.close()
        
    def updatePrice(self, drink, proteins, sideDish, dessert, new_price, calorie):
        # Actualiza el precio de un combo de comida en la base de datos
        cursor = self.connection_string.connection.cursor()
        cursor.execute("UPDATE ComboMeals SET Price = ? WHERE Drink = ? AND Proteins = ? AND SideDish = ? AND Dessert = ? AND Calorie = ?",
                       (new_price, drink, proteins, sideDish, dessert, calorie))
        self.connection_string.connection.commit()
        cursor.close()

