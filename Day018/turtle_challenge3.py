# Draw different shapes

from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()

def draw_shapes(turtle_obj, list_of_sides):
    for s in list_of_sides:
        side_length = s * 8
        angle = 360/s
        for _ in range(s):
            turtle_obj.forward(side_length)
            turtle_obj.right(angle)
            
sides = [x for x in range(3, 11)]
draw_shapes(timmy, sides)
screen.exitonclick()