import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    ticks.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if (reps % 8) == 8:
        countdown(long_break_sec)
        title.config(text='Break', fg=RED)
    elif (reps % 2) == 0:
        countdown(short_break_sec)
        title.config(text='Break', fg=PINK)
    else:
        countdown(work_sec)
        title.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
from math import modf, floor

def countdown(cnt):
    
    cnt_in_mins = cnt/60
    (sec_part, min_part) = modf(cnt_in_mins) # (0.5678000000000338, 1234.0)
    sec_part = floor(sec_part*60)
    min_part = floor(min_part)
    text_to_show = str(min_part).zfill(2) + ':' + str(sec_part).zfill(2)
    
    canvas.itemconfig(timer_text, text=text_to_show)
    if cnt > 0:
        global timer
        timer = window.after(1000, countdown, (cnt-1))
    else:
        if (reps % 2) == 0:
            ticks.config(text=(int(reps/2)) * '✓') 
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = tkinter.Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file='day28_pomodoro_method/tomato.png')
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130,
                                text='00:00',
                                fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# Title
title = tkinter.Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title.grid(row=0, column=1)

# Buttons
start = tkinter.Button(text='Start', highlightbackground=YELLOW, command=start_timer)
start.grid(row=2, column=0, sticky='E')

reset = tkinter.Button(text='Reset', highlightbackground=YELLOW, command=reset_timer)
reset.grid(row=2, column=2, sticky='W')

# Ticks
ticks = tkinter.Label(bg=YELLOW, fg=GREEN)
ticks.grid(row=3, column=1)

window.mainloop()