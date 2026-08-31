class Car:
    def __init__(self,brand ,model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def details(self):
        print(f"{self.brand} is the brand {self.model} model and price is {self.price}")

Car1 = Car("BMW","old","2L")
Car2 = Car("tata","old","1L")
Car3 = Car("OC","New",50000)

Car2.details()


    


        