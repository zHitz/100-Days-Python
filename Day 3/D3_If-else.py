 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = int
if  height >= 120:
    print ("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if age > 18:
        bill = 12
    elif age >= 12 and age <= 18:
        bill = 7
    else:
        bill = 5
    if wants_photo == "Y":
        bill = bill + 3
        print(f"You pay ${bill}")
    else:
        print(f"You pay ${bill}")    
else:
    print("Sorry, you have to grow taller before you can rid")
