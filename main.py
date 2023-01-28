
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

# First dice character to show when the app starts
lbl = Label(App, text=Dice[0], font=('Times', 100))
lbl.grid(row=0, column=0, padx=40)

App.mainloop()