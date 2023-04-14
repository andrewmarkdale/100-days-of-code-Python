# Code to move food around playing area

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
        # Massive brainfarts writing this code
        on_snake = True
        while on_snake:
            flag = False
            xcor = random.randint(-280, 280)
            ycor = random.randint(-280, 280)
            self.coords[0] = xcor
            self.coords[1] = ycor
            for cor in range(0, len(snake.snake)):
                if (self.coords[0]-20 <= snake.snake[cor].xcor() <= self.coords[0]+20
                and self.coords[1]-20 <= snake.snake[cor].ycor() <= self.coords[1]+20):
                    print("on snake!!!")
                    flag = True
                    continue
            if not flag:
               on_snake = False 
            
        self.food.goto(self.coords)
        
    def check_devour(self, snake):
        if (self.coords[0]-20 <= snake.head.xcor() <= self.coords[0]+20
            and self.coords[1]-20 <= snake.head.ycor() <= self.coords[1]+20):
             return True
        return False
        
        