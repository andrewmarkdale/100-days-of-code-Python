"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day: 
3

Project:
Treasure Island Adventure (Choose your own adventure)

Purpose: 
Choose your own adventure game for fun. 

Example:
User chooses between different options, if wrong the user perishes and the game is over.
If the user chooses all options correctly and reaches the treasure, they win and the game
is over.

"""

import random
import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Example flow chart
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


# Variables

left_right = ["left", "right"]
forward_left_right = ["forward", "left", "right"]
colour_choice = ["orange", "green", "blue", "yellow", "red", "purple"]

# Choices

ring = False
first_choice = random.choice(left_right)
second_choice = random.choice(forward_left_right)
third_choice = random.choice(colour_choice)
fourth_choice = random.choice(forward_left_right)
fifth_choice = random.choice(left_right)


# To give player hints for second choice
second_choice_wrong = [x for x in forward_left_right if x != second_choice]
second_choice_wrong1 = random.choice(second_choice_wrong)
second_choice_wrong2 = second_choice_wrong.remove(second_choice_wrong1)


# To give player hints for fourth choice
fourth_choice_wrong = [x for x in forward_left_right if x != fourth_choice]
fourth_choice_wrong1 = random.choice(fourth_choice_wrong)

fifth_choice_wrong = left_right[:]
fifth_choice_wrong.remove(fifth_choice)

print("You awake on a stormy, windy morning. Waves are crashing on the beach not " + 
      "50 yards from the tavern in which you've just spent the night. Your head " +
      "throbs from the previous night of debauchery. Before your journey into the " +
      "jungle in search of Jack Longbeard's treasure.")

print("\nOutside you are approached by a weathered pirate. He asks if you're willing to listen to \
his tale.")


tale = input("\nWill you listen to the pirates tale? Y\\N ")

if tale.lower() == "y":
    
    print("\nThe pirate in this low, gruff voice says, \"Arr, 'tis a black spotted day. Ye'd " + 
          "be wise t' listen smartly. I've been in search o'Longbeard's loot fer a long time now. 'Tis " +
          "fraught wit' danger, traps around every corner. I 'ave made it only part o' the way thar. I " +
          "'ave noted me journey this far. Here, fer ye fer indulgin' an ole pirate.")
    
    print(f"\nThe pirate hands you a piece of paper with his notes. It reads, \n " +
          f"Thar are no monsters t' the {first_choice}. At the next crossroads I 'ave lost two " + 
          f"scallywags venturin' t' the way {second_choice_wrong1}.")
    
    input("Enter any key to continue ")
    
    cow_return = input("\nI merely 'ave a request. Me cap'n once nattered about this golden cow " + 
                       "statue looted from his village as a sprog. It may 'ave some monetary value but 'tis " + 
                       "o' more sentimental value t' me. If ye find it, would ye kindly return it? Y\\N ")
    
    if cow_return.lower() == "y":
        print("I thank ye, take this on yer journey. 'tis me lucky ring, I found it " + 
              "leadin' t' ole Longbeards booty. May it serve ye well.")
        print(f"The old pirate hands you a {third_choice} gemmed ring. You feel a " + 
               "little more confident upon donning the ring.")
        input("Enter any key to continue ")
    else:
        print("'Tis too bad, I wish ye luck on yer journey.")
else:
    print("\"A pox upon ye\", the pirate says in a low, gruff voice.")
    

# First fork in the road
print("\nThe journey begins. The jungle is perilous, filled with snakes and jaguars. " +
"A number of members from your small team have already been lost when you finally come " + 
"upon the first fork in the road. The road forks left and right.")
choice = input("What way will you journey? left/right ")
while True: 
    if choice.lower() != first_choice:
        print(f"You decide to take the {choice} path. Before you know it you're " +
               "sinking in quicksand.")
        if not ring:
            print("You cannot find a way out of the quicksand. You have perished.")
            quit()
        else:
            print("You find a rope to pull yourself out. The old pirate's lucky " +
                  "ring seems to dissapate before you backtrack and choose the correct path.")
            ring = False
    elif choice.lower() == first_choice: 
        print("You seem to have chosen correctly. The path, while initially " +
    "overgrown, quickly opens into a well-groomed path.")
    else:
        
# Second three way fork

print(f"After travelling on the path for a few hours you finally come upon another choice.\
The path goes in three directions: left, right and forward. You suddenly see a flock of\
birds fly away in the {second_choice_wrong2} direction.")
choice = input("What way do you choose? L/R/F ")
if choice != second_choice:
    if not ring:
        print(f"You march on in the {choice} direction. You come upon beasts. Without\
a way to defend yourself you perish.")
        quit() 
    else:
        print(f"You march on in the {choice} direction. You come upon beasts. Luckily, you find\
a sword to defend yourself. Once you've slain the beasts you backtrack and march down the\
correct direction. The old pirate's ring seems to dissapate before your very eyes.")
        

    
