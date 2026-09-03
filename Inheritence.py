class User:
    def __init__(self,username,password = 0):
        self.username = username
        self.__password = password

    def login(self):
        print(f"{self.username} is logged in !") 
class Admin(User):

    def delete_ac(self):
        print(f"{self.username} is the admin logged in !")
        print("Admin deleted the account !")

u = User("Chaithra",123)
u.login()
a = Admin("Vanitha")
a.delete_ac()