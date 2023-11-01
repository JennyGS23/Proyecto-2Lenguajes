# 'Table' class 
from model_Client import Client

class Table:
    def __init__(self):
        self.id = None
        self.cantSeats = None
        self.clientList = None
        self.uniquePay = None
        self.totalPrice = None

    def __str__(self):
        # Custom string representation of Table, combining its attributes.
        return f"{self.id} - {self.cantSeats} - {self.clientList} - {self.uniquePay} - {self.totalPrice}"

    # Getter and Setter for 'id'
    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = newId

    # Getter and Setter for 'cantSeats'
    def getCantSeats(self):
        return self.cantSeats
    
    def setCantSeats(self, newCantSeats):
        self.cantSeats = newCantSeats

    # Getter and Setter for 'clientList'
    def getClientList(self):
        return self.clientList
    
    def setClientList(self, cantClient):
        if not isinstance(cantClient, int) or cantClient < 0:
            raise ValueError("cantClient must be a non-negative integer")

        new_clients = []
        for i in range(cantClient):
            new_client = Client()
            new_client.setId(i) 
            new_clients.append(new_client)

        self.clientList = new_clients

    # Getter and Setter for 'totalPrice'
    def getTotalPrice(self):
        return self.totalPrice

    def setTotalPrice(self, newTotalPrice):
        if isinstance(newTotalPrice, int):
            self.totalPrice = newTotalPrice
        else:
            raise ValueError("Total price must be an integer")
