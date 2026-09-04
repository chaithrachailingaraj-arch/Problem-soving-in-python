class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks

    def display_Info(self):
        print(f"{self.name} Scored {self.marks}")

S1 = Student("chaithra",14)
S2 = Student("chandana",34)


S1.display_Info()