# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if (year % 4)  == 0 :
    if (year % 100) != 0:
        anwser = "Leap Year"
    else:
        if (year % 400 ) == 0:
            anwser = "Leap Year"
        else : 
            anwser = "Not Leap Year"
else:
    anwser = ("Not leap year")
print(anwser)
