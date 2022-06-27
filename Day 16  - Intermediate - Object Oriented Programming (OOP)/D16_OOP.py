# from re import T
# from turtle import Turtle, Screen
# import turtle
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick() 
from base64 import b16decode
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Pokemon", "Type"]
x.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],

    ]
)
# x.set_style(b16decode)
print(x)