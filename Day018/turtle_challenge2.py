# Draw dashed line

from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()

def dashed_line(turtle_obj, dist):
    distance = int(dist/10)
    for _ in range(distance):
        turtle_obj.forward(10)
        if turtle_obj.isdown():
            turtle_obj.penup()
        else:
            turtle_obj.pendown()
    
dashed_line(timmy, 300)
screen.exitonclick()