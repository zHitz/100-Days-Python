rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
import random
choice = [rock, paper, scissors]
computer_choice = int(random.randint(0,2))
print(choice[human_choice])
print(f"Computer chose {choice[computer_choice]}")
if human_choice != computer_choice:
    if human_choice == 0 and computer_choice == 2:
        print("You win")
    elif human_choice == 1  and computer_choice == 0:
        print("You win")
    elif human_choice == 2 and computer_choice == 1:
        print("You win")
    else:
        print("You lose") 
else:
    print("You draw")  
k=input("press close to exit") 

