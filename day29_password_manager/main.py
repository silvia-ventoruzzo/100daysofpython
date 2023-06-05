import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

DEFAULT_USERNAME='silvia@mostcommonemail.com'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    psw_letters = [choice(letters) for _ in range(randint(8, 10))]
    psw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    psw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = psw_letters + psw_symbols + psw_numbers

    shuffle(password_list)
    password = ''.join(password_list)
    
    password_input.delete(0, tkinter.END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    
    data_dict = {'website': website, 'username': username, 'password':password}
    values_ok = []
    for (key, value) in data_dict.items():
        if len(value) == 0 or value.isspace():
            values_ok.append(
                            messagebox.askokcancel(title=website,
                                                   message=f'The {key} input is empty. Do you want to add anyways?')
            )
            
    if sum(values_ok) == len(values_ok):
        data_ok = messagebox.askokcancel(title=website,
                                        message=f'Add the following data?\nUsername: {username}\nPassword: {password}')
        
        if data_ok:
            with open('day29_password_manager/data.txt', 'a') as file:
                file.write(f'{website} | {username} | {password}\n')
            website_input.delete(0, tkinter.END)
            username_input.delete(0, tkinter.END)
            username_input.insert(0, DEFAULT_USERNAME)
            password_input.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Canvas
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_image = tkinter.PhotoImage(file='day29_password_manager/logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

# Labels, entries and buttons
website_text = tkinter.Label(text='Website:')
website_text.grid(row=1, column=0)
website_input = tkinter.Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_text = tkinter.Label(text='Email/Username:')
username_text.grid(row=2, column=0)
username_input = tkinter.Entry(width=40)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, DEFAULT_USERNAME)

password_text = tkinter.Label(text='Password:')
password_text.grid(row=3, column=0)
password_input = tkinter.Entry(width=22)
password_input.grid(row=3, column=1)
password_button = tkinter.Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add_button = tkinter.Button(text='Add', width=38, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()