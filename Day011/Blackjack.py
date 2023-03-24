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
    # Dr. Yu utilizes lists from what I gather but my solution works.
    cards_inplay = {
        'user': [],
        'dealer': []
    }
    print(logo)
    
    # First cards, two for the user and dealer. Dealer only shows one initially.
    for _ in range(2):
        add_card(cards_inplay['user'])
        add_card(cards_inplay['dealer'])
    
    if sum(cards_inplay['user']) == BLACKJACK and sum(cards_inplay['dealer']) == BLACKJACK:
        print_score(cards_inplay)
        print("  That's a standoff! Draw!")
        return
    elif sum(cards_inplay['user']) == BLACKJACK:
        print_score(cards_inplay)
        print("  That's a natural, you win!")
        return
    active_game = True
    while active_game:
        
        # Doing a check like the final example program given
        if is_bust(cards_inplay, 'user'):
            if ACE in cards_inplay['user']:
                cards_inplay['user'][cards_inplay['user'].index(ACE)] = 1
            else:
                # Normally if you bust you auto lose but the example program seemed to have the
                # dealer draw cards after you're bust
                print_score(cards_inplay)
                finish_dealer_hand(cards_inplay)
                print_score(cards_inplay, final=True)
                print("You went over. You lose.")
                break
        
        print_score(cards_inplay)
        another_card = input("Type 'y' to get a new card. Type 'n' to pass: ")
        
        if another_card == 'y':
            add_card(cards_inplay["user"])
            user_sum = sum(cards_inplay['user'])
            if user_sum == BLACKJACK:
                finish_dealer_hand(cards_inplay)
                print_score(cards_inplay, final=True)
                print("Blackjack!")
                if sum(cards_inplay['dealer']) == BLACKJACK:
                    print("Dealer has blackjack as well, draw!")
                else:
                    print("You win!")
                active_game = False
        # Round is over, calculate scores and determine winner.
        elif another_card == 'n':
            finish_dealer_hand(cards_inplay)
            user_sum = sum(cards_inplay['user'])
            dealer_sum = sum(cards_inplay['dealer'])
            
            print_score(cards_inplay, final=True)
            
            # Win/lose conditions
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