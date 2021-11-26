# Morse Code Translator
import tkinter
from tkinter import BOTH, IntVar, DISABLED, END
from PIL import ImageTk, Image
from playsound import playsound

# Define window
root = tkinter.Tk()
root.title("Morse Code Translator")
root.geometry("500x350+100+100")
root.resizable(0, 0)

# Define fonts colors
button_font = ('SimSun', 10)
root_color = "#494949"
frame_color = "#dcdcdc"
button_color = "#ADADAD"
text_color = "#f8f8ff"
root.config(bg=root_color)


# Define functions
def guide():
    global morse
    # Define new window
    root_guide = tkinter.Toplevel()
    root_guide.title("Morse Code")
    root_guide.geometry("350x350+600+100")
    root_guide.config(bg=root_color)
    # Create the image
    morse = ImageTk.PhotoImage(Image.open('morse_chart.JPG'))
    # Create label
    label = tkinter.Label(root_guide, image=morse, bg=frame_color)
    label.pack(padx=10, pady=5, ipadx=5, ipady=5)
    # Create button
    close_button = tkinter.Button(root_guide, text="Close", font=button_font, bg=button_color, command=root_guide.destroy)
    close_button.pack(padx=10, pady=1, ipadx=60)

    # Disabel the guide button
    guide_button.config(state=DISABLED)


def convert():
    # English to morse code:
    if language.get() == 1:
        get_morse()
    elif language.get() == 2:
        get_english()


def get_morse():
    morse_code = ""

    # Get the input text and standardize it to lower case
    text = input_text.get("1.0", END)
    text = text.upper()

    for letter in text:
        if letter not in english_morse.keys():
            text = text.replace(letter, '')

    # Break up into individual words based on space " " and put into a list
    word_list = text.split(" ")

    # Turn each individual word in word_list into a list of letters
    for word in word_list:
        letters = list(word)
        for letter in letters:
            morse_char = english_morse[letter]
            morse_code += morse_char
            morse_code += " "
        morse_code += "|"

    output_text.insert("1.0", morse_code)


def get_english():
    english = ""

    # Get the input text
    text = input_text.get("1.0", END)

    for letter in text:
        if letter not in morse_english.keys():
            text = text.replace(letter, '')

    # Break up into individual words based on | and put into a list
    word_list = text.split("|")

    # Turn each word into a list of letters
    for word in word_list:
        letters = word.split(" ")
        for letter in letters:
            english_char = morse_english[letter]
            english += english_char
        english += " "

    output_text.insert("1.0", english)


def play_morse():
    if language.get() == 1:
        text = output_text.get("1.0", END)
    elif language.get() == 2:
        text = input_text.get("1.0", END)

    for value in text:
        if value == ".":
            playsound("dot.mp3")
            root.after(100)
        elif value == "-":
            playsound('dash.mp3')
            root.after(200)
        elif value == " ":
            root.after(300)
        elif value == "|":
            root.after(700)


def clear():
    input_text.delete(1.0, END)
    output_text.delete(1.0, END)


english_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' ', '|': '|', "": ""}
morse_english = dict([(value, key) for key, value in english_morse.items()])

# Define Layout
# Create frames
input_frame = tkinter.LabelFrame(root, bg=frame_color)
output_frame = tkinter.LabelFrame(root, bg=frame_color)
input_frame.pack(padx=10, pady=(10, 5))
output_frame.pack(padx=10, pady=(5, 10))

# Layout for the input frame
input_text = tkinter.Text(input_frame, bg=text_color, heigh=8, width=30)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

language = IntVar()
language.set(1)
morse_button = tkinter.Radiobutton(input_frame, text="English --> Morse Code", variable=language, value=1, font=button_font, bg=frame_color)
english_button = tkinter.Radiobutton(input_frame, text="Morse Code --> English", variable=language, value=2, font=button_font, bg=frame_color)

morse_button.grid(row=0, column=0, padx=10, pady=(15, 0))
english_button.grid(row=1, column=0)

guide_button = tkinter.Button(input_frame, bg=button_color, font=button_font, text="Guide", command=guide)
guide_button.grid(row=2, column=0, sticky="WE", padx=10)

# Layout for the input frame
output_text = tkinter.Text(output_frame, bg=text_color, heigh=8, width=30)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

convert_button = tkinter.Button(output_frame, bg=button_color, font=button_font, text="Convert", command=convert)
play_morse_button = tkinter.Button(output_frame, bg=button_color, font=button_font, text="Play Morse", command=play_morse)
clear_button = tkinter.Button(output_frame, bg=button_color, font=button_font, text="Clear", command=clear)
quit_button = tkinter.Button(output_frame, bg=button_color, font=button_font, text="Quit", command=root.destroy)

convert_button.grid(row=0, column=0, ipadx=50, padx=10)
play_morse_button.grid(row=1, column=0, sticky="WE", padx=10)
clear_button.grid(row=2, column=0, sticky="WE", padx=10)
quit_button.grid(row=3, column=0, sticky="WE", padx=10)
# Call root window's main loop
root.mainloop()