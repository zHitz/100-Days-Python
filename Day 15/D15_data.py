MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources_data = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

test ={"a":1,"b":2}
test2 ={"b": 3,"a":4}
def a():
    for n in test:
        test[n] = test2[n]
        
a()
print(test)