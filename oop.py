class Human:
    def __init__(self,name="Unknown",age = 0,salary = -1):
        self.name = name
        self.age = age
        self.salary = salary

    def walk(self):
        print(f"{self.name} is walking")

c = Human("Chaithra",19,1)
v = Human("Vanitha",21,1000.8)

print(c.salary)


c.walk()
v.walk()


    

    
