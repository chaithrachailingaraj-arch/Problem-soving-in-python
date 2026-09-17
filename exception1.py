try:
    num = int(input("Enter te value of num :"))
    Result = 10/num
    print(f"Result : {Result}")
except ZeroDivisionError:
    print("Division by zero is not possible because it gives infinite value")
except ValueError:
    print("Invalid input, pleasse enter a number not a string")
