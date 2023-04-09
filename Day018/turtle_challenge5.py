# Spirograph

import turtle as t
import random

screen = t.Screen()
timmy = t.Turtle()

def random_colour():
    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = random.randint(0, 250)
    return (r,g,b)

def draw_spirograph(turtle_obj, radius, num_circles):
    turn = 360/num_circles
    for _ in range(num_circles):
        turtle_obj.color(random_colour())
        turtle_obj.circle(radius)
        turtle_obj.left(turn)

t.colormode(255)
timmy.speed("fastest")
draw_spirograph(timmy, 100, 72)
screen.exitonclick()