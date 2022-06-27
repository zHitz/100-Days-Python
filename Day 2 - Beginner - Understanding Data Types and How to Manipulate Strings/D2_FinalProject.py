from cgi import print_arguments
from decimal import FloatOperation


print("Welcome to the tip calculator.")
totalbill = input("What was the total bill? $")
tip = input("What percaentage tip would you like to give? 10, 12, or 15? ")
people = input("how mane people to split the bill? ")

finalpay = (float(totalbill) + (float(totalbill)* int(tip) /100)) / int(people)
print (finalpay)
finalpay = round(finalpay, 2)
print("Each person should pay: $" + str(finalpay))