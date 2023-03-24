"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
11

Project:
Blackjack

Purpose:
Create a functioning game of blackjack

This is before classes in the course, we're just supposed to use what we've learned so far.

"""

import random
from art import logo
from utils import *

def blackjack_game_loop():
    # Using a dictionary to represent user and dealer hands
    cards_inplay = {}
    print(logo)
    # First cards
    cards_inplay["user"] = [random.choice(cards), random.choice(cards)]
    cards_inplay["dealer"] = [random.choice(cards)]
    
    active_game = True
    while active_game:
        
        # Doing a check like the final example program given
        if is_bust(cards_inplay, 'user'):
            if ACE in cards_inplay['user']:
                cards_inplay['user'][cards_inplay['user'].index(ACE)] = 1
            else:
                print_score(cards_inplay)
                while sum(cards_inplay["dealer"]) < 17:
                    add_card(cards_inplay["dealer"])
                    if is_bust(cards_inplay, "dealer") and ACE in cards_inplay['dealer']:
                        cards_inplay['dealer'][cards_inplay['dealer'].index(ACE)] = 1
                print_score(cards_inplay, final=True)
                print("You went over. You lose.")
                break
        
        print_score(cards_inplay)
        another_card = input("Type 'y' to get a new card. Type 'n' to pass: ")
        
        if another_card == 'y':
            add_card(cards_inplay["user"])
        elif another_card == 'n':
            while sum(cards_inplay["dealer"]) < 17:
                add_card(cards_inplay["dealer"])
                if is_bust(cards_inplay, 'dealer') and ACE in cards_inplay['dealer']:
                    cards_inplay['dealer'][cards_inplay['dealer'].index(ACE)] = 1
                    
                
            user_sum = sum(cards_inplay['user'])
            dealer_sum = sum(cards_inplay['dealer'])
            
            print_score(cards_inplay, final=True)
            
            if dealer_sum > BLACKJACK:
                print(f"Dealer went over, you win!")
            elif user_sum > dealer_sum:
                print("You win!")
            elif user_sum == dealer_sum:
                print("Draw!")
            else:
                print("You lose.")
                
            active_game = False
        else:
            print("Invalid input, please enter 'y' or 'n'!\n")