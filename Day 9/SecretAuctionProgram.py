"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
9

Project:
Secret Auction Program

"""

import os
from art import logo

# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
bidders = {}
    
print(logo)
print("Welcome to the secret auction program.")

while True:
    name = input("Please enter your name: ")
    
    # Ensure integer value
    while True:
        bid = input("Please enter your bid: $")
        if bid.isnumeric():
            break
        else:
            print("\nPlease enter an integer value.")
            
    # Set key value pair in dictionary
    bidders[name] = bid
    
    # Check if repeat auction loop or end auction
    while True:
        print("\nAre there any other bidders?")
        cont = input("Type 'yes' or 'no': ")
        
        # If continue is 'yes' clear the screen and run auction loop again
        if cont == 'yes':
            clear()
            break
        
        # If continue is 'no' check for max value in dictionary, print winner and exit
        elif cont == 'no':
            max_val = 0
            max_name = ""
            for name in bidders:
                if int(bidders[name]) > max_val:
                    max_name = name
                    max_val = int(bidders[name])
            print(f'The winner is of the auction is {max_name} with a bid of ${max_val}')
            quit()
        else:
            print("\nPlease enter a valid response.")
    