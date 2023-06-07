import os
import tkinter
import pandas as pd
from random import choice

os.chdir('day31_flash_cards/')

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError: 
    data = pd.read_csv('data/french_words.csv')

# ---------------------------- NEW CARD ------------------------------- #
def new_card():
    global new_index, flip_timer
    window.after_cancel(flip_timer)
    new_index = choice(data.index)
    new_french = data.loc[new_index, 'French']
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=new_french, fill='black')
    flip_timer = window.after(3000, flip_card)
    
# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    new_english = data.loc[new_index, 'English']
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=new_english, fill='white')

# ---------------------------- DELETE WORDS ------------------------------- #
def drop_word():
    new_card()
    data.drop(index=new_index, inplace=True)
    data.to_csv('data/words_to_learn.csv', index=False)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = tkinter.PhotoImage(file='images/card_front.png')
back_image = tkinter.PhotoImage(file='images/card_back.png')
card_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150,
                                   text='Language',
                                   fill='black',
                                   font=(FONT_NAME, 40, 'italic'))
word_text = canvas.create_text(400, 263,
                               text='Word',
                               fill='black',
                               font=(FONT_NAME, 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
no_image = tkinter.PhotoImage(file='images/wrong.png')
no_button = tkinter.Button(image=no_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,
                           command=new_card)
no_button.grid(row=1, column=0)

yes_image = tkinter.PhotoImage(file='images/right.png')
yes_button = tkinter.Button(image=yes_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0,
                            command=drop_word)
yes_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
new_card()

window.mainloop()