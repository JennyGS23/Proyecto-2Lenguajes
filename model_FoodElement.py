class FoodElement:
    def __init__(self):
        self.name = None
        self.type = None
        self.description = None
        self.dayMoment= None

    def __str__(self):
        return f"{self.name} - {self.type} - {self.description} - {self.dayMoment}"
    
    # Getter of name
    def getName(self):
        return self.name

    # Setter of name
    def setName(self, newName):
        if isinstance(newName, str):
            self.name = newName
        else:
            print("Name must be string")

    # Getter of type
    def getType(self):
        return self.type

    # Setter of type
    def setType(self, newType):
        if isinstance(newType, str):
            self.type = newType
        else:
            print("Type must be string")

    # Getter of description
    def getDescription(self):
        return self.description

    # Setter of description
    def setDescription(self, newDescription):
        if isinstance(newDescription, str):
            self.description = newDescription
        else:
            print("Description must be string")

    # Getter of dayMoment
    def getDayMoment(self):
        return self.dayMoment

    # Setter of dayMoment
    def setDayMoment(self, newDayMoment):
        if isinstance(newDayMoment, str):
            self.dayMoment = newDayMoment
        else:
            print("dayMoment must be string")

class Calorie:
    def __init__(self):
        self.name = None
        self.calories = None

    def __str__(self):
        return f"{self.name} - {self.calories}"

    # Getter of calories
    def getCalories(self):
        return self.calories

    # Setter of calories
    def setCalories(self, newCalorie):
        if isinstance(newCalorie, int):
            self.calories = newCalorie
        else:
            print("Calories must be int")