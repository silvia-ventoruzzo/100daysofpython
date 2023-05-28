from turtle import Turtle, Screen, colormode
import colorgram
from random import choice

# Extract colors from a dot painting from Hirst
color_list = colorgram.extract('day18_hirst_painting/way_to_understand.jpg', 15)
color_list = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in color_list]

# Create a dot 10x10 dot painting
# Dot size = 20, Space size = 50
dot_size = 20
space_size = 50
colormode(255)
dot_painting = Turtle()
dot_painting.speed('fast')
dot_painting.hideturtle()
dot_painting.penup()
dot_painting.setposition(x=-250, y=-250)
dot_painting.pendown()
line_beginning = dot_painting.position()
for n in range(1, 101):
    dot_color = choice(color_list)
    dot_painting.dot(dot_size, dot_color)
    dot_painting.penup()
    # Staying in same line
    if (n % 10) != 0:
        dot_painting.forward(space_size)
    # If line of 10 is finished, jump to next row
    else:
        line_beginning = (line_beginning[0], line_beginning[1]+space_size)
        dot_painting.goto(x=line_beginning[0], y=line_beginning[1])
    dot_painting.pendown()
  
screen = Screen()
screen.exitonclick()
