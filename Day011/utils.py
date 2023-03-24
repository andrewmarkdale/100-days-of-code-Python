
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Constants
# Ace constant, if ace is in hand and sum of hand is over 21, ace in hand becomes 1 
ACE = 11
# Blackjack, ultimate score of game
BLACKJACK = 21

def add_card(dictionary_entry):
    """Takes dictionary key and adds another card"""
    return dictionary_entry.append(random.choice(cards))

# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_score(dict, final=False):
    
    if not final:
        print(f"Your cards: {dict['user']}, current score: {sum(dict['user'])}")
        print(f"Computers first card: {dict['dealer'][0]}")
    else:
        print(f"Your final hand: {dict['user']}, final score: {sum(dict['user'])}")
        print(f"Computer's final hand: {dict['dealer']}, final score: {sum(dict['dealer'])}")
                
def is_bust(dict, player):
    return sum(dict[player]) > BLACKJACK
    