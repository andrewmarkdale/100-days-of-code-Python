from turtle import *

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for square in range(0, 3):
            self.snake.append(Turtle())
            self.snake[square].shape('square')
            self.snake[square].color('white')
            self.snake[square].penup()
            self.snake[square].setx(square * -MOVE_DISTANCE)
            
        
    def move(self):
        for square in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[square-1].xcor()
            new_y = self.snake[square-1].ycor()
            self.snake[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
        
    def up(self):
        self.head.setheading(90)
        
    def down(self):
        self.head.setheading(270)
        
    def right(self):
        self.head.setheading(0)
        
    def left(self):
        self.head.setheading(180)