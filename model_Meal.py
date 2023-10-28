from abc import ABC, abstractmethod

# Abstract Factory Design Pattern: This code defines an abstract class for creating meals.

# Abstract class 'Meal' that acts as the Product in the Abstract Factory pattern.
class Meal(ABC):
    def __init__(self):
        # Common attributes for all meal types.
        self.id = None
        self.protein = None
        self.sideDish = None
        self.dayMoment = None

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def setId(self, newId):
        pass

    @abstractmethod
    def getProtein(self):
        pass

    @abstractmethod
    def setProtein(self, newId):
        pass

    @abstractmethod
    def getSideDish(self):
        pass

    @abstractmethod
    def setSideDish(self, newId):
        pass

    @abstractmethod
    def getDayMoment(self):
        pass

    @abstractmethod
    def setDayMoment(self, newDayMoment):
        pass
