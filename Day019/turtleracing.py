"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
19

Project:
Turtle racing game

Purpose:
Turtles race across screen

"""

import turtle as turt
import random
screen = turt.Screen()
screen.setup(width=500, height=500)

turtles = ["Timmy", "Tommy", "Tammy", "Tiffany", "Timothy", "Trinity"]
colours = ["blue", "violet", "green", "yellow", "orange", "red"]
ypos = [-100, -60, -20, 20, 60, 100]
turt_dict = {}

for d, nc in enumerate(zip(turtles, colours)):
     t = turt.Turtle()
     t.shape("turtle")
     t.penup()
     t.sety(ypos[d])
     t.setx(-screen.window_width()/2 + 40)
     t.color(nc[1])
     turt_dict[nc[0]] = t

user_bet = screen.textinput(title="Make your bet", prompt=f"Out of {', '.join([x for x in colours])} which coloured turtle do you believe will win? ")
race_active = True
while race_active:
    for name in turtles:
        forward_dist = random.randint(1, 5)
        turt_dict[name].forward(forward_dist)
        if(turt_dict[name].xcor() >= screen.window_width()/2):
            race_active = False
            print(f"{name} ({turt_dict[name].color()[0]}) wins this race!")
            if user_bet == turt_dict[name].color()[0]:
                print("You win!")
            else:
                print("You lose!")
            break
screen.exitonclick()