"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
4

Project:
Rock Paper Scissors

Purpose:
To create the game rock paper scissors 

"""

## Starter Code

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

  
'''
#Write your code below this line 👇

import random
import time 
choices = [rock, paper, scissors]
choices_countdown = ["Rock!", "Paper!", "Scissors!"]

print("Welcome to Rock Paper Scissors Python Version")
player_score = 0
computer_score = 0
while True:
    player_choice = input("\nWhat do you choose? Rock, Paper or Scissors: ")
    player_choice = player_choice.lower()
    if player_choice in ['rock', 'paper', 'scissors']:
        computer_choice = random.choice(choices)
        
        for i in range(3):
            print(choices_countdown[i])
            time.sleep(.40)
            
        print("Go!")
        
        # Computer turn
        if computer_choice is rock:
            computer_choice_str = "rock"
            print("\nThe computer plays rock!")
        elif computer_choice is paper:
            computer_choice_str = "paper"
            print("\nThe computer plays paper!")
        else:
            computer_choice_str = "scissors"
            print("\nThe computer plays scissors!")
        print(computer_choice)
        
        # User turn
        if player_choice == "rock":
            print("\nYou played rock!")
            print(rock)
        elif player_choice == "paper":
            print("\nYou played paper!")
            print(paper)
        else:
            print("\nYou played scissors!")
            print(scissors)
            
        if computer_choice_str == player_choice:
            print("\nTie game, no score awarded!")
        else:
            if computer_choice_str == "rock":
                if player_choice == "scissors":
                    print("\nYou lose this round!")
                    computer_score += 1
                else: 
                    print("\nYou win this round!")
                    player_score += 1
            elif computer_choice_str == "paper":
                if player_choice == "rock":
                    print("\nYou lose this round!")
                    computer_score += 1
                else: 
                    print("\nYou win this round!")
                    player_score += 1
            else:
                if player_choice == "paper":
                    print("\nYou lose this round!")
                    computer_score += 1
                else: 
                    print("\nYou win this round!")
                    player_score += 1
        
        print(f"\nCurrent score: Player {player_score} Computer {computer_score}")
        cont = input("\nDo you want to play again? Y/N ")
        if cont.lower() == "n":
            print(f"\nFinal score: Player {player_score} Computer {computer_score}")
            print("Great game!")
            break
    else:
        print("Please choose one of the available options.")