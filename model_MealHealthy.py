from abc import ABC
from model_Meal import Meal  # Import the base class 'Meal'

# 'HealthyMeal' class is a concrete implementation of a meal, extending the abstract 'Meal' class.
class HealthyMeal(Meal):
    def __init__(self):
        super().__init__()  # Initialize the attributes defined in the base class.
        self.drink = None
        self.dessert = None
        self.minCalories = None

    def __str__(self):
        # Custom string representation of Healthy Meal, combining its attributes.
        return f"{self.id} - {self.drink} - {self.protein} - {self.sideDish} - {self.dessert} - {self.minCalories}"
    
    # Getter and Setter for 'id'
    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = newId

    # Getter and Setter for 'drink'
    def getDrink(self):
        return self.drink

    def setDrink(self, newDrink):
        self.drink = newDrink

    # Getter and Setter for 'protein'
    def getProtein(self):
        return self.protein

    def setProtein(self, newProtein):
        self.protein = newProtein

    # Getter and Setter for 'sideDish'
    def getSideDish(self):
        return self.sideDish

    def setSideDish(self, newSideDish):
        self.sideDish = newSideDish

    # Getter and Setter for 'dessert'
    def getDessert(self):
        return self.dessert

    def setDessert(self, newDessert):
        self.dessert = newDessert

    # Getter and Setter for 'dayMoment'
    def getDayMoment(self):
        return self.dayMoment

    def setDayMoment(self, newDayMoment):
        self.dayMoment = newDayMoment

    # Getter and Setter for 'minCalories'
    def getMinCalories(self):
        return self.minCalories

    def setMinCalories(self, newMinCalories):
        self.minCalories = newMinCalories
