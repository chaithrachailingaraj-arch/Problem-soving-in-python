class Mobile:
    def __init__(self,brand,price):
        self.brand = brand 
        self.price = price

    def display(self):
        print(f"{self.brand} costs {self.price}")

M1 = Mobile("Apple",140000)
M1.display()