from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    '''
    Class to create and move snake
    '''
    
    def __init__(self, color='white', part_length=20, head_position=(0,0), initial_length=3):
        self.parts = []
        self.color = color
        self.part_length = part_length
        self.head_position = head_position
        self.initial_length = initial_length
        self.create_snake()
        self.head = self.parts[0]
        
    # Step 1: Create the snake body
    def create_snake(self):
        for n in range(self.initial_length):
            part = Turtle(shape='square')
            part.color(self.color)
            part.penup()
            x_position = self.head_position[0] if n == 0 else x_position
            y_position = self.head_position[1] if n == 0 else y_position
            part.setposition(x=x_position, y=y_position)
            x_position -= self.part_length
            self.parts.append(part)
            
    # Step 2: Move the snake
    def move(self):
        for n in range(len(self.parts)-1, -1, -1):
            part = self.parts[n]
            if n == 0:
                part.forward(self.part_length)
            else:
                previous_part_position = self.parts[n-1].position()
                part.goto(x=previous_part_position[0], y=previous_part_position[1]) 
                
    # Part 3: Control the snake
    # def turn(self, direction):
    #     direction_mapping = {'right': 0, 'up': 90, 'left': 180, 'down': 270}
    #     to_angle = direction[direction.lower()]
    #     self.head.setheading(to_angle)
        
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
    
