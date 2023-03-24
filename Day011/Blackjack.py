"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
11

Project:
Black Jack

Purpose:
Create a functioning game of blackjack

This is before classes in the course, we're just supposed to use what we've learned so far.

"""

import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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
                

def blackjack_game_loop():
    cards_inplay = {}
    print(logo)
    ACE = 11
    # First cards
    cards_inplay["user"] = [random.choice(cards), random.choice(cards)]
    cards_inplay["dealer"] = [random.choice(cards)]
    
    active_game = True
    while active_game:
        
        # Doing a check like the final example program given
        if sum(cards_inplay['user']) > 21:
            if ACE in cards_inplay['user']:
                cards_inplay['user'][cards_inplay['user'].index(ACE)] = 1
            else:
                print_score(cards_inplay)
                while sum(cards_inplay["dealer"]) < 17:
                    add_card(cards_inplay["dealer"])
                    if sum(cards_inplay["dealer"]) > 21 and ACE in cards_inplay['dealer']:
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
                if sum(cards_inplay["dealer"]) > 21 and ACE in cards_inplay['dealer']:
                    cards_inplay['dealer'][cards_inplay['dealer'].index(ACE)] = 1
                    
                
            user_sum = sum(cards_inplay['user'])
            dealer_sum = sum(cards_inplay['dealer'])
            
            print_score(cards_inplay, final=True)
            
            if dealer_sum > 21:
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
            
                
                    
                
                
            
    
    
    
    
if __name__ == '__main__':
    play = True
    while play == True:
        play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_game == 'y':
            clear()
            blackjack_game_loop()
        elif play_game == 'n':
            print("Have a nice day!")
            play = False
        else:
            print("Invalid input!\n")