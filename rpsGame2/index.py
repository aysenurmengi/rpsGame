import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from random import randint
import os

root = tk.Tk()
root.title("Rock - Paper - Scissors")
root.geometry("400x400")

base_dir = os.path.dirname(__file__)
icon_dir = os.path.join(base_dir, '.venv', 'image')
icon_names = ['rock', 'paper', 'scissors']
icons = {name: ImageTk.PhotoImage(Image.open(os.path.join(icon_dir, f'{name}.png')).resize((50, 50), Image.LANCZOS)) for name in icon_names}

score = 0
options = ['rock', 'paper', 'scissors']
def play(user):
    global score
    computer_choice = options[randint(0, 2)]
    result = ""


    if user == computer_choice:
        print("You drew!")
    elif user == 'rock':
        if computer_choice == 'paper':
            score -= 1
            result="You lose! Paper wraps rock."
        else:
            score += 1
            result="You win! Rock breaks scissors."
    elif user == 'paper':
        if computer_choice == 'scissors':
            score -= 1
            result="You lose! Scissors cuts paper."
        else:
            score += 1
            result="You win! Paper wraps rock."
    elif user == 'scissors':
        if computer_choice == 'rock':
            score -= 1
            result="You lose! Rock breaks scissors."
        else:
            score += 1
            result="You win! Scissors cuts paper."
    messagebox.showinfo("Result",
                        f"You chose: {user}\nComputer chose: {computer_choice}\n\n{result}\n\nCurrent score: {score}")


def exit_game():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", exit_game)


for name in icon_names:
    tk.Button(root, text=name.capitalize(), image=icons[name], compound=tk.TOP, bg="#c9cbfd", command=lambda name=name: play(name)).pack(pady=13)

tk.Button(root, text="Exit", bg = "#d21b18" , command=exit_game).pack(pady=25)

root.mainloop()
