name = input("\nEnter your name :")
marks =int(input("Enter your total marks in PUC : "))

with open("Marks.txt","a") as file1:
    file1.write(f"Student name :{name} \n Marks :{marks}\n ")

    print("Marks added successfully !")

