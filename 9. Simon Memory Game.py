# Simon Memory Code
import tkinter
from tkinter import IntVar, ACTIVE, NORMAL, DISABLED
import random
# Define window
root = tkinter.Tk()
root.title("Simon Memory Code ")
root.geometry("400x400")
root.resizable(0, 0)


#  Define fonts and colors
game_font1 = ('Arial', 12)
game_font2 = ('Arial', 10)
white = "#c6cbcd"
white_light = "#fbfcfc"
magenta = "#90189e"
magenta_light = "#f802f9"
cyan = "#078384"
cyan_light = "#00fafa"
yellow = "#9ba00f"
yellow_light = "#f7f801"
root_color = "#2eb4c6"
game_color = "#f6f7f8"
root.config(bg=root_color)

# Set global variables for the game
time = 500
score = 0
game_sequence = []
player_sequence = []


# Define functions
def pick_sequence():
    while True:
        value = random.randint(1, 4)
        if len(game_sequence) == 0:
            game_sequence.append(value)
            break
        elif value != game_sequence[-1]:
            game_sequence.append(value)
            break

    play_sequence()


def play_sequence():
    change_label("Playing!")

    delay = 0
    for value in game_sequence:
        if value == 1:
            root.after(delay, lambda: animate(white_button))
        elif value == 2:
            root.after(delay, lambda: animate(magenta_button))
        elif value == 3:
            root.after(delay, lambda: animate(cyan_button))
        elif value == 4:
            root.after(delay, lambda: animate(yellow_button))
        delay += time


def animate(button):
    button.config(state=ACTIVE)
    root.after(time, lambda: button.config(state=NORMAL))


def change_label(message):
    game_button.config(text=message)
    if message == "Wrong!":
        game_button.config(bg="red")
    else:
        game_button.config(bg=game_color)


def difficulty():
    global time
    if difficulty.get() == 'Easy':
        time = 1000
    elif difficulty.get() == 'Medium':
        time = 500
    else:
        time = 200


def press(value):
    player_sequence.append(value)
    if len(player_sequence) == len(game_sequence):
        check_round()


def check_round():
    global player_sequence
    global game_sequence
    global score
    if player_sequence == game_sequence:
        change_label("Correct!")
        score += len(player_sequence) + int(1000/time)
        root.after(500, pick_sequence())
    else:
        change_label("Wrong!")
        score = 0
        disable()
        game_sequence = []
        root.after(2000, lambda: change_label("New Game"))
    player_sequence = []
    score_label.config(text="Score: " + str(score))


def disable():
    white_button.config(state=DISABLED)
    magenta_button.config(state=DISABLED)
    cyan_button.config(state=DISABLED)
    yellow_button.config(state=DISABLED)


def enable():
    white_button.config(state=NORMAL)
    magenta_button.config(state=NORMAL)
    cyan_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)

    pick_sequence()


# Define Layout
# Create frames
into_frame = tkinter.Frame(root, bg=root_color)
game_frame = tkinter.LabelFrame(root, bg=game_color)

into_frame.pack()
game_frame.pack()

# Layout for the into frame
game_button = tkinter.Button(into_frame, text="New Game", font=game_font1, command=enable)
score_label = tkinter.Label(into_frame, text="Score: " + str(score), bg=root_color, font=game_font1)
game_button.grid(row=0, column=0, padx=10, pady=10, ipadx=30)
score_label.grid(row=0, column=1, padx=10, pady=10)

# Layout for the game frame
white_button = tkinter.Button(game_frame, bg=white, activebackgroun=white_light, borderwidth=3, state=DISABLED, command=lambda: press(1))
magenta_button = tkinter.Button(game_frame, bg=magenta, activebackgroun=magenta_light, borderwidth=3, state=DISABLED, command=lambda: press(2))
cyan_button = tkinter.Button(game_frame, bg=cyan, activebackgroun=cyan_light, borderwidth=3, state=DISABLED, command=lambda: press(3))
yellow_button = tkinter.Button(game_frame, bg=yellow, activebackgroun=yellow_light, borderwidth=3, state=DISABLED, command=lambda: press(4))

white_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
magenta_button.grid(row=0, column=2, columnspan=2,  padx=10, pady=10, ipadx=60, ipady=50)
cyan_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)
yellow_button.grid(row=1, column=2,  columnspan=2, padx=10, pady=10, ipadx=60, ipady=50)

difficulty_label = tkinter.Label(game_frame, bg=game_color, text="Difficulty:", font=game_font2)
difficulty_label.grid(row=2, column=0, padx=2)

difficulty = IntVar()
difficulty.set(2)
easy_radio = tkinter.Radiobutton(game_frame, text="Easy", bg=game_color, variable=difficulty, value=1)
medium_radio = tkinter.Radiobutton(game_frame, text="Medium", bg=game_color, variable=difficulty, value=2)
hard_radio = tkinter.Radiobutton(game_frame, text="Hard", bg=game_color, variable=difficulty, value=3)

easy_radio.grid(row=2, column=1, padx=2)
medium_radio.grid(row=2, column=2, padx=2)
hard_radio.grid(row=2, column=3, padx=2)

# Call root window's main loop
root.mainloop()
