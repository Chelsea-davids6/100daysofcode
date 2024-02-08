from tkinter import *
import random

# Initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Rock, Paper, Scissors')
root.config(bg='seashell3')

# Heading
Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()

# User choice
user_take = StringVar()
Label(root, text='Choose any one: rock, paper, scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)

# Computer choice
choices = ["rock", "paper", "scissors"]
comp_pick = random.choice(choices)

# Function to play
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie, you both selected the same.')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You lose, computer selected paper.')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You win, computer selected scissors.')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You lose, computer selected scissors.')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You win, computer selected rock.')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You lose, computer selected rock.')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You win, computer selected paper.')
    else:
        Result.set('Invalid: choose any one -- rock, paper, scissors')

# Function to reset
def reset():
    Result.set('')
    user_take.set('')

# Function to exit
def exit_game():
    root.destroy()

# Button
Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50).place(x=25, y=250)
Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=exit_game).place(x=230, y=310)

root.mainloop()
