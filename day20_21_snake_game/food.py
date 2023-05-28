from turtle import Turtle
from random import randint

class Food(Turtle):
    '''
    Class to create food for the snake to eat.
    '''
    
    def __init__(self, color='blue', relative_size=0.5):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=relative_size, stretch_wid=relative_size)
        self.color(color)
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x=random_x, y=random_y) 