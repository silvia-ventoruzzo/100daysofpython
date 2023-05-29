from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, position=(0,0)):
        super().__init__()
        self.initial_position = position
        self.color('white')
        self.shape('circle')
        self.penup()
        self.setposition(x=position[0], y=position[1])
        self.x_move = 10
        self.y_move = 10     
        self.move_speed = 0.1   
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed += 0.9
        
    def reset_position(self):
        self.goto(x=self.initial_position[0], y=self.initial_position[1])
        self.move_speed = 0.1
        self.bounce_x()