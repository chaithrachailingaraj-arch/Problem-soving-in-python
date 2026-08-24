import random
choices=["Rock","Paper","Scissor"]

#Input from user
user=input("Enter Rock,Paper,Scissor: ")

# computer random choice
computer=random.choice(choices)

if user==computer:
    print(" its Tie 😑")

elif (user == "Rock" and computer == "Scissor") or \
     (user == "Paper" and computer == "Rock") or \
     (user == "Scissor" and computer == "Paper"):
     print("You win🔥")

else:
     print("Computer wins🔥")


