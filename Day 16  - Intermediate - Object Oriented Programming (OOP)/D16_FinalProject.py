
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Coffee_Maker = CoffeeMaker()
Money_Machine = MoneyMachine()
my_Menu = Menu()

#Print Report:
def report():
    Coffee_Maker.report()
    Money_Machine.report()
    
def resources_sufficient(choice):
    return Coffee_Maker.is_resource_sufficient(choice)

def main():
    is_on = True 
    while is_on:
        choice = input("​What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False    
        elif choice == "report":
            report()
        else:      
            the_drink = my_Menu.find_drink(choice)
            if Coffee_Maker.is_resource_sufficient(the_drink) and Money_Machine.make_payment(the_drink.cost):
                Coffee_Maker.make_coffee(the_drink)
    
main()



