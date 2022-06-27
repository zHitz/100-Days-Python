
import random
from D12_art import logo
    
#Compare number
def guess(your_number, number):
    if number == your_number:
        return "win"
    elif number < your_number:
        print("Too high.")
        print("Guess again.")
        return attempt - 1
    else:
        print("Too low.")
        print("Guess again.")
        return attempt - 1
 
#Choie easy or hard    
def choice():
    level = input("Choose a diffculty. Type 'easy' or 'hard': ")
    if level == "easy":
        attempt = 10
        return attempt
    else:
        attempt = 5
        return attempt

play_game = True
attempt = 0
number = random.randint(1, 101)

#main 
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of number between 1 and 100.") 
attempt = choice()
while play_game ==  True:
    print(f"You have {attempt} remaining to guess the number.")
    your_number = int(input("Make a guess: "))
    attempt = guess(your_number, number)
    if attempt == "win":
        print (f"You got it! The answer was {number}")
        play_game = False
    else:
        if attempt == 0:
            print(f"You've run out of guesses, you lose. The anwser is {number}")
            play_game = False
            