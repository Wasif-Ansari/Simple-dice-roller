
from tkinter import *

App = Tk()
App.title("Dice Roller")

Dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

def roll():
    from random import randint
    dice_choice = randint(1, 6)

    dice_lbl = Label(App, text=Dice[dice_choice], font=('Times', 100), width=2)
    dice_lbl.grid(row=0, column=0, padx=40)


# First dice character to show when the app starts
lbl = Label(App, text=Dice[0], font=('Times', 100))
lbl.grid(row=0, column=0, padx=40)


roll_button = Button(App, text='Roll', command=roll)
roll_button.grid()

App.mainloop()