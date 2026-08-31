class Student:
    def __init__(self,name, USN, marks):
        self.name = name
        self.USN = USN
        self.marks = marks

    def details(self):
        print(f"{self.name} is her name")
        print(f"{self.USN} is her USN")
        print(f"{self.marks} is her marks")

Information = Student("Chaithra"," 4GH25CS025 ",9.2)

Information.details()


        
        