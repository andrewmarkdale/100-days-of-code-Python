from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()
def draw_square(turtle_object, dist):
    for i in range(4):
        turtle_object.forward(dist)
        turtle_object.left(90)
    

draw_square(timmy, 200)
screen.exitonclick()