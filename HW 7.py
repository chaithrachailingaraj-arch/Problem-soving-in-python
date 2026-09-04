# Inheritence

class Vehicle:
    def start(self):
        print("Vehicle Starting ...")

class Bike(Vehicle):
    def __init__(self, name):
        self.name = name
    def ride(self):
        print("Riding....")    

B = Bike("Royal Enfield")
B.ride()
B.start()
