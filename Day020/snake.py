from turtle import *

MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
LAST = -1
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
    
    def add_square(self):
        self.snake.append(Turtle())
        self.snake[LAST].shape('square')
        self.snake[LAST].color('white')
        self.snake[LAST].penup()
        
            
        
    def move(self):
        for square in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[square-1].xcor()
            new_y = self.snake[square-1].ycor()
            self.snake[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)