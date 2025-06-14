# Project 2 from Nick Walter's "Python for Programmers Course" on udemy
# Hangman Game
import random
import csv

words = ["apple", "book", "desk", "pen", "cat", "dog", "tree", 
         "house", "car", "phone", "computer", "laptop", "keyboard", 
         "mouse", "chair", "table", "door", "window", "wall", "floor"]

# possible expansion: use a csv + random module, pick a random word from larger list
# def pick_word():
# another expansion, print out the guessed letters in order with blanks for 
# un guessed letters / and maybe a print score function showing the letters you guessed
# incorrectly so far

def hangman(lives, word):
    chars = list(word.lower())
    letters_remaining = len(set(chars))
    lives_left = lives
    letters_guessed = []
    incorrect_guesses = []

    # variable representing the state of the word (_ are unguessed letters)
    word_state = ["_" for c in chars]

    while letters_remaining > 0 and lives_left > 0:
        # at the top of the round, print current word state
        print("\nWord: " + " ".join(word_state))

        guess = input("Guess a letter: ").lower()

        # make sure guess is a letter (non-empty, non whitespace, non numeric)
        if not guess or not guess.isalpha() or len(guess) != 1:
            print("Please enter a letter.")
            continue
        
        # check if the user already guessed the letter
        if guess in letters_guessed:
            print(f"Good try, but you already guessed {guess}... try again!")
            continue
        #if correct guess
        elif guess in chars:
            letters_guessed.append(guess)

            # Reveal all positions with the guessed letter
            for i, char in enumerate(chars):
                if char == guess:
                    word_state[i] = guess 

            letters_remaining -= 1
            print(f"Correct! You have {letters_remaining} letters to guess")
            
            if letters_remaining == 0:
                return(f"Congrats, you won with {lives_left} lives remaining! The word was {word}!")
 
        else:
            incorrect_guesses.append(guess)
            lives_left -= 1
            print(f"Incorrect...You have {lives_left} lives left and {letters_remaining} letters to guess")
    
    return(f"You lose! The word was {word}!")

def run_hangman_game():
    numlives = int(input("Enter desired number of lives: "))
    print("Picking a random word...")
    word = random.choice(words)
    print("Let's play hangman!")

    print(hangman(numlives, word))

run_hangman_game()

