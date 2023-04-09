# Random walk

import turtle as t
import random

screen = t.Screen()
timmy = t.Turtle()

#colours = ["cornflower blue", "forest green", "dark cyan", "peru", "goldenrod", "plum", "bisque", "turquoise"]
def random_colour():
    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = random.randint(0, 250)
    return (r,g,b)


def random_walk(turtle_obj, total_walk_dist, colours=[]):
    walk_sections = total_walk_dist // 30
    angles = [0, 90, 180, 270]
    for _ in range(walk_sections):
        #colour = random.choice(colours)
        angle = random.choice(angles)
        turtle_obj.color(random_colour())
        turtle_obj.setheading(angle)
        turtle_obj.forward(30)
        
timmy.pensize(15)
timmy.speed("fastest")
t.colormode(255)
random_walk(timmy, 1500)
screen.exitonclick()
    