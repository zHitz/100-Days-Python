############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random
import os
from D11_art import logo

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = True
money = 500

while play_game == True:
    ai_card_1 = random.choice(cards)
    ai_card_2 = random.choice(cards)
    if ai_card_1 == "A":
        ai_card_1 = 11
    if ai_card_2 == "A":
        ai_card_2 = 11
    ai_cards = ai_card_1 + ai_card_2
    ai_cards_list = [ai_card_1, ai_card_2]
    ai_num_cards= 2

    my_card_1 = random.choice(cards)
    my_card_2 = random.choice(cards)
    if my_card_1 == "A":
        my_card_1 = 11
    if my_card_2 == "A":
        my_card_2 = 11
    my_cards = my_card_1 + my_card_2
    my_cards_list =[my_card_1, my_card_2]
    my_num_cards=2

    hit = True

    # Continues or not?
    begin = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if begin == "y":
        os.system('cls')
        print(logo)
        print(f"You have ${money}, If you win +$100, you lose -$100")

    elif begin == "m":
        print(f"You have ${money}")
    else:
        play_game = False

    # Blackjack:  
    if ai_cards == 21 or (ai_card_1 == 11 and ai_card_2 == 11) and ai_num_cards == 2:
        print(f"    Computer's final card: {ai_cards_list}, current score {ai_cards}")
        print(f"    Your card {my_cards_list}, current score: {my_cards}") 
        print("You lose, Computer Win with a BlackJack")
        money -= 100 
    elif my_cards == 21 or (my_card_1 == 11 and my_card_2 == 11) and my_num_cards == 2:
        print(f"    Computer's final card: {ai_cards_list}, current score {ai_cards}")
        print(f"    Your card {my_cards_list}, current score: {my_cards}") 
        print("Win with a BlackJack")
        money += 100
    else:

        #My function
        while hit == True:
            print(f"    Computer's first card: {ai_cards_list[0]}")
            print(f"    Your card {my_cards_list}, current score: {my_cards}")
            choice = input("Type 'y' to get another card, type 'n' to pass:")
            if choice == "y" and my_num_cards <= 5 and my_cards <= 21:
                my_next_card = random.choice(cards)
                if my_next_card == "A" and (my_cards + 11 > 21):
                    my_cards_list.append(1)
                    my_cards += my_cards_list[my_num_cards]
                    my_num_cards +=1
                elif my_next_card == "A" and (my_cards + 11 <= 21):
                    my_cards_list.append(11)
                    my_cards += my_cards_list[my_num_cards]
                    my_num_cards +=1      
                else:
                    my_cards_list.append(my_next_card)
                    my_cards += my_cards_list[my_num_cards]
                    my_num_cards +=1
            else :
                hit = False
                for n in range(len(my_cards_list)-1) :
                    if my_cards_list[n] == 11:
                        my_cards_list = 1
                        hit = True
            for n in range(len(my_cards_list)-1) :
                    if my_cards_list[n] == 11 and my_cards > 21:
                        my_cards_list[n] = 1
                        my_cards = my_cards -10
                        hit = True
            if my_cards > 21:
                hit = False
        if choice == "n":
            #AI function        
            ai_hit = True
            ai_num_cards = 2
            while ai_hit == True:
                if ai_cards < 17 and ai_cards <21 and ai_num_cards <=5:
                    ai_next_card = random.choice(cards)
                    if ai_next_card == "A" and (ai_cards + 11 > 21):
                        ai_cards_list.append(1)
                        ai_cards += ai_cards_list[ai_num_cards]
                        ai_num_cards +=1
                    elif ai_next_card == "A" and (ai_cards + 11 <= 21):
                        ai_cards_list.append(11)
                        ai_cards += ai_cards_list[ai_num_cards]
                        ai_num_cards +=1    
                    else:
                        ai_cards_list.append(ai_next_card)
                        ai_cards += ai_cards_list[ai_num_cards]
                        ai_num_cards +=1
                else :
                    ai_hit = False

        # Result
        print(f"    Computer's final card: {ai_cards_list}, current score {ai_cards}")
        print(f"    Your card {my_cards_list}, current score: {my_cards}")  
        if my_cards > 21 and ai_cards > 21:
            print("You Draw")
        elif my_cards <= 21 and ai_cards >21:
            print("Opponet went over. You win")
            money += 100
        elif my_cards > 21 and ai_cards <= 21:
            print("You went over, You lose")
            money -= 100    
        else:    
            if my_cards > ai_cards:
                print("You win")
                money += 100
            elif my_cards == ai_cards:
                print("You draw")
            else :
                print("You lose")
                money -= 100
    if money == 0:
        os.system('cls')
        print(logo)
        print(f" You have ${money}, You lose GoodBye")
