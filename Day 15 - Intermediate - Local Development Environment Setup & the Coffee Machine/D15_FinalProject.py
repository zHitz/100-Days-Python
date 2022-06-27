#TODO print report
#TODO check resources
#TODO process coins
#TODO check transaction
#TODO make coffe

from D15_data   import resources_data, MENU


def report(resources,money):
    milk = resources["milk"]
    coffee = resources["coffee"]
    water = resources["water"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coins_inserted = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    print(coins_inserted)
    return coins_inserted

def transaction(choice,resources):
    the_drink = MENU[choice]
    cost = the_drink["cost"]
    ing = the_drink["ingredients"]
    water = ing["water"]
    milk = ing["milk"]
    coffee = ing["coffee"]
    
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]
    water_left = resources["water"]
    
    if water > water_left:
        print("Sorry there is not enough water.")
        return FUND - MONEY
    elif milk > milk_left:
        print("Sorry there is not enough milk.")
        return FUND - MONEY
    elif coffee > coffee_left:
        print("Sorry there is not enough coffee.")
        return FUND - MONEY
    elif MONEY < cost:
        print("Sorry that's not enough money. Money refunded")
        return FUND - MONEY
    else:
        money_left = round(MONEY - cost,2)
        print(f"Here is ${money_left} in change")
        print(f"Here is your {choice} Enjoy!")
        return FUND + cost

def re(choice):
    the_drink = MENU[choice]
    ing = the_drink["ingredients"]
    resources["water"] -= ing["water"]
    resources["milk"]  -= ing["milk"]
    resources["coffee"]  -= ing["coffee"]
    return resources
    
coffee_machine = True
FUND = 0
resources = resources_data    
while coffee_machine == True:            
    your_choice = input("What would you like? (espresso/latte/cappuccino):")
    if your_choice == "report":
        report(resources, FUND)
    else:
        MONEY = process_coins()   
        FUND = transaction(your_choice,resources)
        re(your_choice)
           


            