"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
11

Project:
Number guessing game

Purpose:
User tries to guess a randomly generated number
Game has two modes, hard and easy.
Hard: 5 guesses
Easy: 10 guesses

"""

import random
from art import logo
import os

# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def guessing_game(guesses):
    number  = random.randint(1, 101)
    game_active = True
    while game_active:
        guess = input("Make a guess: ")
        if guess.isnumeric():
            guess = int(guess)
            if guess == number:
                print(f"You got it! The answer was {number}")
                game_active = False
            else: 
                low = guess < number
                if low:
                    print("Too low")
                else:
                    print("Too high")
            
                guesses -= 1
                if guesses > 0:
                    print("Guess again")
                    print(f"You have {guesses} attempts remaining to guess the number.")
                else:
                    print(f"You have run out of guesses. You lose. The number was {number}")
                    game_active = False
        else:
            print("Invalid input! Please enter an integer.")
                
        
def game_loop():

    still_playing = True
    while still_playing:
        clear()
        print("Welcome to the number guessing game!")
        print(logo)
        valid_input = False
        while not valid_input:
            mode = input("Would you like to play on hard or easy mode? ")
            if mode.lower() == 'hard':
                guesses = 5
                valid_input = True
            elif mode.lower() == 'easy':
                guesses = 10
                valid_input = True
            else:
                print("Invalid input! Please enter 'easy' or 'hard'.")
                
        guessing_game(guesses)
        
        valid_input = False
        while not valid_input:
            cont = input("Would you like to continue playing? y/n: ")
            if cont == 'n':
                print("Have a nice day!")
                still_playing = False
                valid_input = True
            elif cont == 'y':
                valid_input = True
            else:
                print("Invalid input! Please enter 'y' or 'n'.")
            
