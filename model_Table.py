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
    
    def setClientList(self, newClientList):
        if isinstance(newClientList, Client[]):
            self.clientList = newClientList
        else:
            print("ClientList must be a list of client")

    # Getter and Setter for 'uniquePay'
    def getUniquePay(self):
        return self.uniquePay

    def setUniquePay(self, newUniquePay):
        if isinstance(newName, bool):
            self.uniquePay = newUniquePay
        else:
            print("UniquePay must be bool")
