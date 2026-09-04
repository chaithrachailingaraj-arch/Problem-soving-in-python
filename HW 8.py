class Shape:
    def calculate_Area(self):
        print("Area calculated ")

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        

    def calculate_Area(self):
        print(f"Area of cirlce is {3.14*self.radius**2}")

class rectangle(Shape):
    def __init__(self, breadth,height):
        self.breadth = breadth
        self.height = height

    def calculate_Area(self):
        print(f"Area of rectanglE is {self.breadth * self.height}")

C = circle(5)    
R = rectangle(3,5)

C.calculate_Area()
R.calculate_Area()