#Password Generator Project
from email.contentmanager import raw_data_manager
import random
from this import s
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
Pass_letters = ""
Pass_number = ""
Pass_symbols = ""
for n in range (1,nr_letters +1):
    Pass_letters += letters[random.randint(0,int(len(letters)-1))]
for n in range (1,nr_numbers +1):
    Pass_number += numbers[random.randint(0,int(len(numbers)-1))]
for n in range (1,nr_symbols +1):
    Pass_symbols += symbols[random.randint(0,int(len(symbols)-1))]
PassWord = Pass_letters + Pass_symbols + Pass_number
# print(f"Here is your password: {PassWord}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
Password_List = list(PassWord)
print(Password_List)
random_password = ""
for n in range(1,int(len(PassWord))+1 ):
    Lenght = int(len(Password_List))
    position = random.randint(0,Lenght-1)
    random_password += str(Password_List[position])
    Password_List.remove(Password_List[position])
print(f"Here is your password: {random_password}")
