from turtle import Turtle, Screen
import numpy as np
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = list(np.linspace(start=-150, stop=150, num=len(colors)))

turtles = []
for n in range(len(colors)):
    t = Turtle(shape='turtle')
    t.color(colors[n])
    t.penup()
    t.setposition(x=-230, y=y_positions[n])
    turtles.append(t)
    
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race? Enter a color:')
    
if user_bet is not None:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        distance = randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 220:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                title = "You've won"
            else:
                title = "You've lost"            
            screen.textinput(title=title, prompt=f'The {winning_color} turtle is the winner. Press OK to close the game.')
            screen.bye()





