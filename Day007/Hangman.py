"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
7

Project:
Hangman game

Purpose:
To create a working version of the hangman game in python

"""


import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Example list of potential words to be guessed
# word_list = ["aardvark", "baboon", "camel"]

# Using a list of the most popular 7 letter words from
# https://github.com/powerlanguage/word-lists/blob/master/1000-most-common-words.txt

with open("words.txt") as words:
    chosen_word = random.choice(words.readlines()).rstrip().lower()

# The randomly chosen word to be guessed
blank_list = ["_" for x in chosen_word]
char_flag = False
stage = 1
already_guessed = ""
# Game loop
while True:
    print(stages[-stage])
    print("\n" + " ".join(blank_list))
    print(f"Letters guessed thus far: {already_guessed if already_guessed != '' else 'No letters have been guessed as of yet'}")
    # Getting the users guess
    guess = input("\nGuess a letter to see if it's in the chosen word: ").lower()
    if len(guess) == 1 and guess.isalpha(): 
        
        if guess in already_guessed:
            print(f"You have already guessed {guess}, please choose another letter.")
        # Check if user has entered single letter
        else:
            already_guessed += guess
            for i in range(len(chosen_word)):   
                if guess == chosen_word[i]:
                    # Set blank space to the guess
                    blank_list[i] = guess 
                    char_flag = True

            if char_flag:
                print(f"Your guess of {guess} was in the chosen word!")
                if "".join(blank_list) == chosen_word:
                    print("\n" + " ".join(blank_list))
                    print(f"Letters guessed thus far: {already_guessed if already_guessed != '' else 'No letters have been guessed as of yet'}")
                    print(f"You win! The chosen word was {chosen_word}.")
                    break
            else:
                print(f"Your guess of {guess} was not in the chosen word.")
                stage += 1
                if stage == len(stages):
                    print(stages[-stage])
                    print(f"\nYou've lost the game! The chosen word was {chosen_word}.")
                    break
            
            char_flag = False
    else:
        print("\nPlease enter a single alphabetic character!")
#print(f"The chosen word was {chosen_word}")
