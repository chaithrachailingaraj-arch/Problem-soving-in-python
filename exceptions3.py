try:
    Groom = input("Who she will marry ? - ")

    if Groom.lower() != "john":
        raise Exception(" She tell that ,I can't marry him😒")
except Exception as e:
    print(f"Error :{e}")
else:
    print("She tell that ,I am ready to marry him😁")



