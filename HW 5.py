class Bankaccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        if self.__balance > 5000000:
            print("Bank is filled with 50L of amount")
        else:
            self.__balance += amount
            print(f"Deposited suuccessfully ! {self.__balance}")

            
    def withdraw(self,amount):
        if self.__balance < amount:
           print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withrawn successfully ! {self.__balance}")
        
A = Bankaccount("1234",100)
A.check_balance()
A.deposit(13000)
A.withdraw(100)


