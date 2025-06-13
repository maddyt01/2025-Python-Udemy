# Project 2 from Nick Walter's "Python for Programmers Course" on udemy
# Hangman Game
import random
import csv

words = ["apple", "book", "desk", "pen", "cat", "dog", "tree", 
         "house", "car", "phone", "computer", "laptop", "keyboard", 
         "mouse", "chair", "table", "door", "window", "wall", "floor"]

#possible expansion: use a csv + random module, pick a random word from larger list
#def pick_word():

def hangman(lives, word):
    chars = list(word.lower())
    letters_remaining = len(chars)
    lives_left = lives
    letters_guessed = []

    while letters_remaining > 0 and lives_left > 0:
        guess = input("Guess a letter: ").lower()

        if(guess in chars) and (guess not in letters_guessed):
            letters_guessed.append(guess)
            numchars = chars.count(guess)
            letters_remaining -= numchars
            print(f"Correct! You have {letters_remaining} letters to guess")
        elif guess in letters_guessed:
            print(f"Good try, but you already guessed {guess}... try again!")
            continue
        else:
            lives_left -= 1
            print(f"Incorrect...You have {lives_left} lives left and {letters_remaining} letters to guess")
        
        if lives_left == 0:
            return(f"You lose! The word was {word}!")
        elif letters_remaining == 0:
            return(f"Congrats, you win! The word was {word}!")

def run_hangman_game():
    numlives = int(input("Enter desired number of lives: "))
    print("Picking a random word...")
    word = random.choice(words)
    print("Let's play hangman!")

    print(hangman(numlives, word))

run_hangman_game()

