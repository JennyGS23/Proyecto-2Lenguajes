# 'Order' class 
class Order:
    def __init__(self):
        self.id = None
        self.meal = None
        self.price = None

    def __str__(self):
        # Custom string representation of Order, combining its attributes.
        return f"{self.id} - {self.meal} - {self.price}"

    # Getter and Setter for 'id'
    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = newId

    # Getter and Setter for 'meal'
    def getMeal(self):
        return self.meal
    
    def setMeal(self, newMeal):
        self.meal = newMeal

    # Getter and Setter for 'price'
    def getPrice(self):
        return self.price
    
    def setPrice(self, newPrice):
        self.price = newPrice
