#8th
name=input("Enter your name:")
age=int(input("ENTER AGE:"))
Percentage=float(input("Enter percentage:"))
print(type(name))
print(type(age))
print(type(Percentage))

#9th

a=10
b=23
temp=0
temp=a
a=b
b=temp
print("a:",a)
print("b:",b)

#10th 

a=10
b=20
# a,b=b,a

c=a+b
a=c-a
b=c-b
print("a:",a)
print("b:",b)

# 11th - Type conversion
num=input("Enter num:")
print(int(num))
print(float(num))
print(str(num))

#12th 
price=int(input("enter price of item:"))
quantity=int(input("Enter quantity:")) 

Total_price=price*quantity

print(Total_price)

#13TH

A=int(input("Enter a:"))
B=int(input("Enter b:"))
print(A/B)
print(A%B)

#14TH

n=int(input("Enter n:"))
if n%2==0:
    print("Even")
else:
    print("Odd")
