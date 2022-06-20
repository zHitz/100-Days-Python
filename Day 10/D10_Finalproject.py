import os
from D10_art import logo
print(logo)

#Calc

#add
def add(x,y):
    return x + y

#subtract
def subtract  (x,y):
    return x - y

#multiply
def multiply(x,y):
    return x * y

#divide
def divide(x,y):
    return x / y
operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

New_calc = True
while New_calc == True:
    re_calc = True
    num1 = round(int(input("What's  the first number? ")),1)
    for symbol in operations:
        print(symbol)
    while re_calc == True :   
        operations_symbols = input("Pick an operation : ")
        num2 = round(int(input("What's  the next number? ")),1)    
        calc_function = operations[operations_symbols]
        anwser = round(calc_function(num1, num2),1)
        print(f"{num1} {operations_symbols} {num2} = {anwser} ")
        num1 = anwser
        cont = input(f"Type 'y' to continues calculating with {anwser}, or type 'n' to start a new calculation: ")
        if cont == "n":
            os.system('cls')
            re_calc = False


