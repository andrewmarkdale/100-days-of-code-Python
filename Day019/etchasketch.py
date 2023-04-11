# Etch-a-sketch project from day 19
# Andrew Dale
# Day 19

import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()

def move_forward():
    timmy.forward(10)
    
def move_backward():
    timmy.backward(10)
    
def turn_right():
    timmy.right(5)
    
def turn_left():
    timmy.left(5)
    
def clear_screen():
    timmy.clear()
    
def reset_screen():
    timmy.reset()

screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="r", fun=reset_screen)
t.listen()
screen.exitonclick()