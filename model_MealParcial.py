from abc import ABC
from model_Meal import Meal  # Import the base class 'Meal'

# 'ParcialMeal' class is a concrete implementation of a meal, extending the abstract 'Meal' class.
class ParcialMeal(Meal):
    def __init__(self):
        super().__init__()  # Initialize the attributes defined in the base class.
        self.price = None
    def __str__(self):
        # Custom string representation of Parcial Meal, combining its attributes.
        return f"{self.id} - {self.protein} - {self.sideDish} - {self.price} - {self.calorie}"

    # Getter and Setter methods for 'id'
    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    # Getter and Setter methods for 'protein'
    def getProtein(self):
        return self.protein

    def setProtein(self, newProtein):
        self.protein = newProtein

    # Getter and Setter methods for 'sideDish'
    def getSideDish(self):
        return self.sideDish

    def setSideDish(self, newSideDish):
        self.sideDish = newSideDish

    # Getter and Setter methods for 'price'
    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    # Getter and Setter methods for 'calorie'
    def getCalorie(self):
        return self.calorie

    def setCalorie(self, newCalorie):
        self.calorie = newCalorie
