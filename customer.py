from atm_card import *

class Customer:
    def __init__(self,id,custPin = 1234,custBalance = 10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def getID(self):
        return self.id
    
    def getPin(self):
        return self.custPin

    def getBalance(self):
        return self.custBalance

    def withdraw(self,nominal):
        self.custBalance -= nominal

    def deposit(self,nominal):
        self.custBalance += nominal