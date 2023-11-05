# 'Bill' class 
class Bill:
    def __init__(self):
        self.id = None
        self.date = None
        self.client = None
        self.order = None
        self.price = None

    def __str__(self):
        # Custom string representation of Bill, combining its attributes.
        return f"{self.id}"

    # Getter and Setter for 'id'
    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = newId

    # Getter and Setter for 'date'
    def getDate(self):
        return self.date
    
    def setDate(self, newDate):
        self.date = newDate

    # Getter and Setter for 'client'
    def getClient(self):
        return self.client
    
    def setClient(self, newClient):
        self.client = newClient

    # Getter and Setter for 'order'
    def getOrder(self):
        return self.order
    
    def setId(self, newOrder):
        self.order = newOrder


    # Getter and Setter for 'price'
    def getPrice(self):
        return self.price
    
    def setPrice(self, newPrice):
        self.price = newPrice
