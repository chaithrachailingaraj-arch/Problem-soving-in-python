
Friend1 =input(f"Enter your frd1 name :  ")
Friend2=input(f"\nEnter your frd2 name :  ")
Friend3=input(f"\nEnter your frd3 name :  ")

with open("friends.txt","w") as frd_file:
    frd_file.write(f"{Friend1}\n")
    frd_file.write(f"{Friend2}\n")
    frd_file.write(f"{Friend3}\n")
print("Friend added to file successfuly !")
    

    
        