# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
number_of_names = int(len(names) - 1)
name_choice = names[random.randint(0,number_of_names)]
print(name_choice + " is going to buy the meal today!")


