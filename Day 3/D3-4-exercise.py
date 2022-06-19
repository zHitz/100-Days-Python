# 🚨 Don't change the code below 👇
from audioop import add


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill_size =  0
billpp = 0
billc = 0
bill = 0
if size == "S":
    bill_size = 15
    if add_pepperoni == "S":
        billpp = 2
elif size == "M":
    bill_size = 20
else:
    bill_size = 25        
if add_pepperoni == "Y"  and (size == "M" or size == "L"):
    billpp = 3
if extra_cheese == "Y":
    billc = 1
bill = bill_size + billc + billpp
print(f"Your final bill is: {bill}$")


