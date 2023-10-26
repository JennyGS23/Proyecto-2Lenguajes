class FoodElement:
    def __init__(self, id, type, description, dayMoment):
        self.name = name
        self.type = type
        self.description = description
        self.dayMoment= dayMoment

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
