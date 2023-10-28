# 'Client' class 
class Client:
    def __init__(self):
        self.id = None
        self.order = None

    def __str__(self):
        # Custom string representation of Client, combining its attributes.
        return f"{self.id}"

    # Getter and Setter for 'id'
    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = newId

    # Getter and Setter for 'Order'
    def getOrder(self):
        return self.order
    
    def setId(self, newOrder):
        self.order = newOrder
