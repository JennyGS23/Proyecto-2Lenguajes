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
            id, drink, protein, sideDish, dessert, dayMoment= row
            meal = ComboMeal()
            meal.setId(id)
            meal.setDrink(drink)
            meal.setProtein(protein)
            meal.setSideDish(sideDish)
            meal.setDessert(dessert)
            meal.setDayMoment(dayMoment)
            meals.append(meal)
        cursor.close()
        return meals
    
    def setMeal(self, drink, protein, sideDish, dessert, dayMoment):
        # Add a new meal to the database
        cursor = self.connection_string.connection.cursor()
        print(drink, protein, sideDish)
        cursor.execute("INSERT INTO ComboMeals (drink, protein, sideDish, dessert, dayMoment) VALUES (?, ?, ?, ?, ?, ?)",
                       (drink, protein, sideDish, dessert, dayMoment))
        self.connection_string.connection.commit()
        cursor.close()

# Create an instance of FoodElementDAO
#dao = MealDAO(connection_string)

# Retrieve food elements and calorie information
#meals = dao.getMeal()

#dao.setMeal(new_drink, new_protein, new_sideDish, new_dessert, new_dayMoment, new_minCalories)

# Close the database connection
#dao.connection_string.connection.close()