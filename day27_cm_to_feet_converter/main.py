import tkinter

window = tkinter.Tk()
window.title('Cm to Feet Converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
input = tkinter.Entry(width=10)
input.grid(row=0, column=1)
input.focus()

cm_label = tkinter.Label(text='Centimeters')
cm_label.grid(row=0, column=2, sticky='W')

# Result
feet_text = tkinter.Label(text='is equal to')
feet_text.grid(row=1, column=0, sticky='E')

feet_value = tkinter.Label(text='')
feet_value.grid(row=1, column=1)
feet_label = tkinter.Label(text='Feet')
feet_label.grid(row=1, column=2, sticky='W')

# Button
def button_clicked():
    cm_value = input.get()
    feet = round(int(cm_value) * 0.0328084, 1)
    feet_value.config(text=str(feet))
button = tkinter.Button(text='Calculate', command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()