from turtle import Turtle, Screen, colormode

# Start
timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

##############################
# Challenge 1: Draw a square #
##############################
square = Turtle()
square.shape('square')
square.shapesize(10, 10, 1)
square.fillcolor('white')

# That was not the correct solution
# They didn't want just a square, but a arrow that closes into a square

###################################
# Challenge 2: Draw a dashed line #
###################################
dashed_line = Turtle()
for _ in range(15):
    dashed_line.forward(10)
    dashed_line.penup()
    dashed_line.forward(10)
    dashed_line.pendown()
    
######################################
# Challenge 3: Draw different shapes #
######################################
from random import randint
colormode(255)
shapes = Turtle()
for n_sides in range(3, 11):
    shapes.color(randint(0, 255),
                 randint(0, 255),
                 randint(0, 255))
    angle = 360/n_sides
    for _ in range(n_sides):
        shapes.forward(100)
        shapes.right(angle)
        
#######################################
# Challenge 4: Generate a random walk #
#######################################
from random import choice
color_list = ['red', 'green', 'blue', 'yellow', 'black', 'orange', 'brown', 'purple', 'pink']
angle_list = [0, 90, 180, 270]
random_walk = Turtle()
random_walk.pensize(5)
for _ in range(100):
    random_walk.color(choice(color_list))
    random_walk.setheading(choice(angle_list))
    random_walk.forward(30)  

##################################
# Challenge 5: Draw a spirograph #
##################################
# Apparently the random color is what I had done before by googling an idea that I had
from random import randint
spirograph = Turtle()
spirograph.speed('fastest')
colormode(255)
size_of_gap = 5
for _ in range(int(360/size_of_gap)):
    spirograph.color(randint(0, 255),
                     randint(0, 255),
                     randint(0, 255))
    spirograph.circle(100)
    spirograph.setheading(spirograph.heading()+size_of_gap)


# This goes at the end of the program
screen = Screen()
screen.exitonclick()