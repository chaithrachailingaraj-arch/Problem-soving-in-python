a = int(input("Enter thhe value of a :"))
b = int(input("Enter thhe value of b :"))

try:
    print(a/b)
    
except Exception as e:
    print(f"Error occurs : {e}")
else:
    print("No error occurs")
finally:
    ("Program ended !")

