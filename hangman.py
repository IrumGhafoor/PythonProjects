#Python Project 3: Hangman Game

#Hangman game is a classic word game 
#How this whole game works:
#The program randomly selects a word from a list of secret words
#the player has limited chances to guess the word
#when a correct letter is guessed, it is revelead in its correct position
#the player wins if all letters are guessed before running out of chances

import random 
from collections import Counter 

words = '''kiwi mango apple banana strawberr coconut cherry'''
words = words.split('')

word = random.choice(words)

if __name__ == '__main__':
    print('Guess the word! HINT: Word is a fruit.')
    
    for _in word:
        print('_', end='')
    print()
    
    letterGuessed = ' '
    chances = len(word) + 2 #mango (5 letters), 7 chances 
    flag = 0
    try:
        while chances > 0 and flag == 0:
            print()
            chances -= 1 
            try:
                guess = input('Enter a letter to guess:').lower()
            except:
                print('Enter only a letter!')
                continue
            if not guess.isalpha():
                print('Enter only a letter')
                continue
            elif len(guess) > 1:
                print('Enter only a single letter!')
                continue
            elif guess in letterGuessed:
                print('You alread guessed that letter!')
                continue 
            if guess in word:
                letterGuessed += guess * word.count(guess)
                for char in word:
                    if char in letterGuessed:
                        print(char, end='')
                    else:
                        print('_', end='')
                        if Counter(letterGuessed) == Counter(word):
                            print("\nCongratulations! You guessed the word:", word)
                            flag = 1
                            break 
                        if chances <= 0 and 
                        Counter(letterGuessed) != Counter(word):
                            print('\n You lost! The word was:', word)
                        except KeyboardInterrupt:
                            print('\n Game interrupted. Bye!')
                            exit()                         