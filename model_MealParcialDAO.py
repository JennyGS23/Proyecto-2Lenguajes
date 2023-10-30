import pyodbc
from controller_Main import DatabaseConnection
from model_MealParcial import ParcialMeal

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
        cursor.execute("SELECT * FROM ParcialMeals")
        for row in cursor:
            id, protein, sideDish, dayMoment= row
            meal = ParcialMeal()
            meal.setId(id)
            meal.setProtein(protein)
            meal.setSideDish(sideDish)
            meal.setDayMoment(dayMoment)
            meals.append(meal)
        cursor.close()
        return meals


    def setMeal(self, protein, sideDish, dayMoment):
        # Add a new meal to the database
        cursor = self.connection_string.connection.cursor()
        cursor.execute("INSERT INTO ParcialMeals (protein, sideDish, dayMoment) VALUES (?, ?, ?, ?)",
                       (protein, sideDish, dayMoment))
        self.connection_string.connection.commit()
        cursor.close()

# Create an instance of FoodElementDAO
#dao = MealDAO(connection_string)

# Retrieve food elements and calorie information
#meals = dao.getMeal()

#dao.setMeal(new_drink, new_protein, new_sideDish, new_dessert, new_dayMoment, new_minCalories)

# Close the database connection
#dao.connection_string.connection.close()