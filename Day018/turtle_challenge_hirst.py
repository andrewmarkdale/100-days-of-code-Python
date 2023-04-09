import turtle as t
import colorgram as cg
import random

timmy = t.Turtle()
screen = t.Screen()


def draw_hirst(turtle_obj, num_colors, img, num_dots):
    
    colours = cg.extract(img, num_colors)
    colours = [(rgb.rgb.r,rgb.rgb.g,rgb.rgb.b) for rgb in colours]
    
    turtle_obj.penup()
    turtle_obj.setheading(225)
    turtle_obj.forward(300)
    turtle_obj.setheading(0)
    
    
    for i in range(1, num_dots):
        turtle_obj.dot(30, random.choice(colours))
        turtle_obj.forward(50)
        if i % 10 == 0:
            turtle_obj.setheading(90)
            turtle_obj.forward(50)
            turtle_obj.setheading(180)
            turtle_obj.forward(500)
            turtle_obj.setheading(0)
    
    turtle_obj.dot(30, random.choice(colours))

timmy.speed('fastest')
timmy.hideturtle()
t.colormode(255)
draw_hirst(timmy, 10, "100daysofcode/Day018/hirst.jpg", 100)
screen.exitonclick()
