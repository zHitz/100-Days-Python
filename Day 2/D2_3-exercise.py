# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
years_end = 90
years_left = (years_end - age_int)
month_left = (years_left *12)
weeks_left = (years_left * 52)
days_left = (years_left * 365)

print("You have " + str(days_left) + " days, " + str(weeks_left) + " weeks, and " + str(month_left)  + " months left.")
2