# Not the most useful exercises but I figured I would follow along.

# from turtle import Turtle, Screen

# def spiral(dist, rot):
#     timmy.forward(dist)
#     timmy.left(rot)
# my_screen = Screen()
# my_screen.setworldcoordinates(-1, -1, my_screen.window_width() - 1, my_screen.window_height() - 1)

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")

# #timmy.forward(100)
# #timmy.left(45)
# dist = my_screen.canvwidth/2
# angle = 80
# while dist > 0.002:
#     spiral(dist, angle)
#     dist *= 0.75
#     angle *= 0.75

# timmy.hideturtle()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
print(table)