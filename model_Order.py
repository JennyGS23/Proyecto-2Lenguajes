# 'Order' class 
class Order:
    def __init__(self):
        self.id = None
        self.dessert = None

    def __str__(self):
        # Custom string representation of Combo Meal, combining its attributes.
        return f"{self.id} - {self.drink} - {self.protein} - {self.sideDish} - {self.dessert} - {self.dayMoment}"

    # Getter and Setter for 'id'
    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = newId
