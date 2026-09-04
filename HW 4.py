class Employee:
    def __init__(self, name, designation, salary = 30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_details(self):
        print(f"{self.name} is {self.designation} his/her salary is {self.salary}")

E1 = Employee("Chaithra","student")
E2 = Employee("Vanitha", "Nurse",45000)
E1.display_details()
E2.display_details()