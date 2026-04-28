#Python Project 2:Python Project 
#Word Guessing Game 

#User has to guess the characters in a randomly selected word
#within a limited number of attempts 
#The program provides feedback after each guess
#Helping the user to either complete the word
#or lose the game based on their guesses 

import random 

name = input("What is your name?")
print("Good Luck!", name)

#List of words for choosing a random word
words = ['rainbow', 'banana', 'computer', 'programming',
         'coding', 'python', 'mathematics', 
         'player', 'condition', 'reverse', 'water',
         'programandprogramming']

word = random.choice(words)
#Prompt the user to guess the word
print("Guess the characters")

#Initialize guesses and turns 
guesses = ' '
turns = 3 

#The main loop 

while turns >0:
    failed = 0 
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("__")
            failed += 1 
    if failed == 0:
        print("You Win!")
        print("The word is:", word)
        break 
    print()
    guess = input("Guess a character:")
    guesses += guess  

if guess not in word:
    turns -= 1
    print("Wrong")
    print("You have", + turns, 'more guesses')

if turns == 0:
    print("You lose!")
