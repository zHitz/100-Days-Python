import os
from D9_art import logo

stt_price = 0
if_continue = True
temp_dict = {}
temp_list =[]
largest_price = 0

#Print logo from art.py
print(logo)


while if_continue == True:
    user = input("What's your name? ")
    price = int(input("What's your bid? "))
    next = input("Are ther any other bidders? Type 'yes' or 'no'. ")

    #dictionary = {price: user}  
    temp_dict[price] = user

    #largest price inthe auction:
    if price > largest_price:
        largest_price = price

    #countinue or not    
    if next == "no":
        if_continue = False

    #clear screen        
    os.system('cls')

#name of the winner
the_winner = temp_dict[largest_price]
#print the result
print(f"The winner is {the_winner} with a bid of ${largest_price}.")