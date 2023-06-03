# This is done using Turtle
# But can it be done with a better visualisation library?

import os
import pandas as pd
from turtle import Turtle, Screen

os.chdir('./day25_us_states_game/project/')

# Create Turtle object with image of the US States
screen = Screen()
screen.title('Do you know all U.S. States?')

image = 'blank_states_img.gif'
screen.addshape(image)
image_turtle = Turtle(shape=image)
text_turtle = Turtle()
text_turtle.hideturtle()
text_turtle.penup()

# Get all location of the states
state_positions = pd.read_csv('50_states.csv')

correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f'{len(correct_guesses)}/50 States Correct',
                                    prompt="What's another U.S. State?")
    answer_state = answer_state.lower()

    # If correct, show state name in the positions from the csv
    state_info = state_positions[state_positions['state'].str.lower() == answer_state]
    if not state_info.empty:
        location = tuple(state_info[['x', 'y']].itertuples(index=False, name=None))[0]
        name = state_info['state'].iat[0]
        correct_guesses.append(name)
        # text_turtle.penup()
        text_turtle.goto(location)
        text_turtle.write(name, True, align="center")
        
    # Exit game if answer exit
    if answer_state == 'exit':
        state_positions[~state_positions['state'].isin(correct_guesses)]['state'].to_frame().to_csv('states_to_learn.csv')
        break