
from D14_data import data
from D14_art import logo, vs
import random
import os

#Identify if id reurn informantion ,else return follower count
def identify(user,id_or_count):
    dict = user
    name = dict["name"]
    fl_count = dict["follower_count"]
    des = dict ["description"]
    country = dict["country"]
    if id_or_count == "id":
        id = (f"{name}, a {des}, from {country}.\n")
        return id
    else:
        return fl_count

#choice random from data
def random_user():
    user = random.choice(data)
    return user

#compare A and B
def compare(ran1, ran2, choice):
    if choice == "A" and ran1 > ran2:
        return True
    elif choice == "B" and ran2 > ran1:
        return True
    else:
        return False


def game():
    game_should_countinue = True
    score = 0
    
    while game_should_countinue == True:
        os.system('cls')
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")    
        user1_id = identify(random_user(),"id")
        user1_fl = identify(random_user(),"fl")
        print(f"Compare A: {user1_id}")
        print(vs)
        user2_id = identify(random_user(),"id")
        user2_fl = identify(random_user(),"fl")
        print(f"Against B: {user2_id}")
        choice= input("Who has more followers? Type 'A' or 'B': ")
        anwser = compare(user1_fl, user2_fl, choice)
        if anwser == True :
            score += 1
            
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_countinue = False

game()
            
            
            
    
    
    
