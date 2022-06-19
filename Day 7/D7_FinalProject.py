import random
import os
from telnetlib import STATUS
from traceback import print_list 
import hangman_wordlist
import hangman_art


# word_list = ["ardvark","baboon","camel"]
word = list(random.choice(hangman_wordlist.word_list))
num_char = int(len(word))
anwser = ""
current_status = 0
wrong_anwser = 0
lives = 6
lose = 0

#change anser to ____:
for n in range(1,num_char+1):
    anwser += "_"
list_anwser = list(anwser)
os.system('cls')
print(hangman_art.logo)

#Core Game

while not current_status  ==  1:
    #Print current answer
    anwser = ' '.join(map(str, list_anwser))
    print(f"{anwser} \n") 

    #if char not in list print this:
    if wrong_anwser == 1:
        print(f"You guessed {your_char}, that's not in the word. you lose a life.")
        lives -=1
    wrong_anwser = 1
    print(hangman_art.stages[lives+1])

    #Input char      
    your_char = input("\nGuess a letter: ")

    #search char in list then add to anwser guess and print curent anwser
    for n in range (1, num_char + 1):
        if your_char == list_anwser[n-1]:
            print(f"You already guessed {your_char}")
        if your_char == word[n-1]:
            list_anwser[n-1] = word[n-1]
            wrong_anwser = 0   
        anwser = ''.join(map(str, list_anwser))
        print(list_anwser[n-1])
    
    #clear 
    os.system('cls') 

    #check the user win or lose
    if list_anwser == word:
        current_status = 1
    if lives == 0 :
        current_status = 1
        lose = 1    
anwser = ' '.join(map(str, list_anwser))   
if lose == 1:
    print(f"{anwser} ")
    print(hangman_art.stages[lives])
    print("You die")

else:
    print(f"{anwser} \n You win.")        