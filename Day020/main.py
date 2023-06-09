"""

Andrew Dale

Subject/Class:
100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu

Day:
20

Project:
Snake

Purpose:
Create the game Snake using OOP in 3 different classes.

"""

from turtle import *
from snake import Snake
from food import Food
import time

        
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
    

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#food.make_food(snake)
game_active = True    
while game_active:
    snake.move()
    screen.update()
    if food.check_devour(snake):
        snake.add_square()
    time.sleep(0.075)


screen.exitonclick()