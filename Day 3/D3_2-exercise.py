# 🚨 Don't change the code below 👇
from telnetlib import BM


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = ( weight / (height **2))
BMIr = round(BMI)

if BMI < 18.5 :
    you = ("You are inderweight")
elif BMI >= 18.5 and BMI < 25:
    you = ("You have a normal weight")
elif BMI >= 25 and BMI < 30:
    you = ("You are slightly overweight")
elif BMI >= 30 and BMI < 35:
    you = ("You are obese")
else:
    you = ("You are clinically obsese")
print("Your BMI is " + str(BMIr) + ", " + you)
