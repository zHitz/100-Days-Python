# 🚨 Don't change the code below 👇
from itertools import count
import turtle


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
namelower= name.lower()
true= name.count('t') + name.count('r') + name.count('u') + name.count('e') 
love= name.count('l') + name.count('o') + name.count('v') + name1.count('e')
truelove = int(str(true) + str(love))
if truelove <= 10 or truelove >= 90:
    print(f"Your score is {truelove}, you go together like coke and mentos.")
elif truelove >= 40 and truelove <= 50:
    print(f"Your score is {truelove}, you are alright together.")
else:   
    print(f"Your score is {truelove}")


