# Code to move food around playing area

from turtle import *
import random



class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.coords = [0, 0]
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
        
    # def make_food(self, snake):
    #     # Massive brainfarts writing this code
    #     on_snake = True
    #     while on_snake:
    #         flag = False
    #         xcor = random.randint(-280, 280)
    #         ycor = random.randint(-280, 280)
    #         self.coords[0] = xcor
    #         self.coords[1] = ycor
    #         for cor in range(0, len(snake.snake)):
    #             if (self.coords[0]-20 <= snake.snake[cor].xcor() <= self.coords[0]+20
    #             and self.coords[1]-20 <= snake.snake[cor].ycor() <= self.coords[1]+20):
    #                 print("on snake!!!")
    #                 flag = True
    #                 continue
    #         if not flag:
    #            on_snake = False 
            
    #     self.food.goto(self.coords)
        
    def check_devour(self, snake):
        if (self.coords[0]-20 <= snake.head.xcor() <= self.coords[0]+20
            and self.coords[1]-20 <= snake.head.ycor() <= self.coords[1]+20):
             return True
        return False
        
        