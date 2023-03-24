"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
14

Project:
Higher Lower

"""

from art import logo, vs
from data import data
import random
import os

VOWELS = ['a', 'e', 'i', 'o', 'u']
# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_data():
    return random.choice(data)

def format_print(choice, letter):
    c_string = ""
    c_string += f"Compare {letter}: "
    c_string += f"{choice['name']}, "
    c_string += f"{'an' if choice['description'][0].lower() in VOWELS else 'a'} "
    c_string += f"{choice['description']} from {choice['country']}"
    print(c_string)
    
def game_loop():
    clear()
    score = 0
    choice_a = get_data()
    print(logo)
    game_active = True
    while game_active:
        choice_b = get_data()
        while choice_a == choice_b:
            choice_b = get_data()
            
        ans = 'A' if choice_a['follower_count'] > choice_b['follower_count'] else 'B'
        format_print(choice_a, 'A')
        print(vs)
        format_print(choice_b, 'B')
        valid_input = False
        while not valid_input:
            guess = input("Who has more followers? Type 'A' or 'B': ")
            if guess.upper() == 'A' or guess.upper() == 'B':
                valid_input = True
                if guess.upper() == ans:  
                    score += 1
                    clear() 
                    print(logo)
                    print(f"You're right! Current score: {score}")
                else:
                    clear()
                    print(logo)
                    print(f"Sorry, that's wrong. Final score: {score}")
                    game_active = False
            else:
                print("Invalid input. Please answer either 'A' or 'B'!")
        choice_a = choice_b
        