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

from Blackjack import *
from utils import *


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