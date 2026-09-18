# A simple mini project just for my reference - This Idea randomly come to my mind
#Problem ststement - On the light of your room it shhows it is ON or not 
# I take 1st swith as 1st Room number not taken in random switch and random room 
# Just to learn * try * except * else * finally

try:
    switch = input("Enter switch you ON : ")
    Room_number = input("Enter your room number :")

    if switch != Room_number:
        raise Exception("You enterred wrong room light ❌")
except Exception as e:
    print(f"Error : {e}")
except ValueError as V:
    print("Enter an integer not string ❌")
else:
    print("You ON the correct switch and Power is ON in your room ✅")
finally:
    print("You touch the switch")

