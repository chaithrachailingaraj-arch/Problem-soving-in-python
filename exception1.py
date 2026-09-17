try:
    num = int(input("Enter te value of num :"))
    Result = 10/num
    print(f"Result : {Result}")
except ZeroDivisionError as Z:
    print(f" {Z} :Division by zero is not possible because it gives infinite value")
except ValueError as V:
    print(f" {V} : Invalid input, please enter a number not a string")
except Exception:
    print("Error")
finally:
    print("program Ended ")

