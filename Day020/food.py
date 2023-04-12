from turtle import *
import random

class Food:
    def __init__(self, snake) -> None:
        self.coords = [0, 0]
        self.food = Turtle("circle")
        self.food.color("blue")
        self.food.penup()
        self.make_food(snake)
        
    def make_food(self, snake):
        xcor = random.randint(-300, 300)
        ycor = random.randint(-300, 300)
        self.coords[0] = xcor
        self.coords[1] = ycor
        self.food.goto(self.coords)
        
    def check_devour(self, snake):
        if (self.coords[0]-5 <= snake.head.xcor() <= self.coords[0]+5
            and self.coords[1]-5 <= snake.head.ycor() <= self.coords[1]+5):
             return True
        return False
        
        