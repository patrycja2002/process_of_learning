# Color Theme Maker
import tkinter
from tkinter import BOTH, IntVar, filedialog

# Define window
root = tkinter.Tk()
root.title("Color Theme Maker")
root.geometry("450x500")
root.resizable(0, 0)


# Define functions
def update_color(v):
    color_c = "#%02x%02x%02x" % (int(red_slider.get()), int(green_slider.get()), int(blue_slider.get()))
    color_box.config(bg=color_c)
    color_hex.config(text=color_c)
    color_tuple.config(text=("(" + str(red_slider.get()) + ") " + "(" + str(green_slider.get()) + ") " + "(" + str(
        blue_slider.get()) + ")"))


def set_color(r, g, b):
    red_slider.set(r)
    green_slider.set(g)
    blue_slider.set(b)


def store_color():
    color_c = "#%02x%02x%02x" % (int(red_slider.get()), int(green_slider.get()), int(blue_slider.get()))
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()
    # Create new widgets for the stored color.
    recall_button = tkinter.Button(output_frame, text="Recall Color", command=lambda: set_color(red, green, blue))
    new_color_tuple = tkinter.Label(output_frame, text=("   ( " + str(red_slider.get()) + " )" + " ( " + str(green_slider.get()) + " )" + " ( " + str(blue_slider.get()) + " )    "))
    new_color_hex = tkinter.Label(output_frame, text=color_c)
    new_color_black_box = tkinter.Label(output_frame, bg='black', width=3, height=1)
    new_color_box = tkinter.Label(output_frame, bg=color_c, width=3, height=1)

    # Put new widgets on the screen
    recall_button.grid(row=color.get(), column=1, padx=10)
    new_color_tuple.grid(row=color.get(), column=2, pady=1)
    new_color_hex.grid(row=color.get(), column=3, padx=10)
    new_color_black_box.grid(row=color.get(), column=4, pady=2, ipadx=5, ipady=5)
    new_color_box.grid(row=color.get(), column=4, ipadx=1, ipady=1)

    # Update the dict stored_colors with the new color tuple and hex values
    colors[color.get()] = [new_color_tuple.cget("text"), new_color_hex.cget("text")]

    if color.get() < 5:
        color.set(color.get() + 1)


def save():
    file_name = filedialog.asksaveasfilename(initialdir='./', title='Save Colors',
                                             filetypes=(('Text', '.txt'), ('All Files', '*.*')))
    with open(file_name, 'w') as f:
        f.write("Color Theme Maker Output\n")
        for saved_entry in colors.values():
            f.write(saved_entry[0] + "\n" + saved_entry[1] + "\n\n")

# Define Layout
input_frame = tkinter.LabelFrame(root, padx=5, pady=5)
output_frame = tkinter.LabelFrame(root, padx=5, pady=5)
input_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)


# Setting up the input frame.
# Create the labels, sliders, and buttons for each color RGB
red_label = tkinter.Label(input_frame, text="R")
red_slider = tkinter.Scale(input_frame, from_=0, to=255, command=update_color)
red_button = tkinter.Button(input_frame, text="Red", command=lambda: set_color(250, 0, 0))

green_label = tkinter.Label(input_frame, text="G")
green_slider = tkinter.Scale(input_frame, from_=0, to=255, command=update_color)
green_button = tkinter.Button(input_frame, text="Green", command=lambda: set_color(0, 250, 0))

blue_label = tkinter.Label(input_frame, text="B")
blue_slider = tkinter.Scale(input_frame, from_=0, to=255, command=update_color)
blue_button = tkinter.Button(input_frame, text="Blue", command=lambda: set_color(0, 0, 250))

red_label.grid(row=0, column=0, sticky='W')
red_slider.grid(row=1, column=0, sticky='W')
red_button.grid(row=2, column=0, padx=1, pady=1, ipadx=12)

green_label.grid(row=0, column=1, sticky='W')
green_slider.grid(row=1, column=1, sticky='W')
green_button.grid(row=2, column=1, padx=1, pady=1, ipadx=10)

blue_label.grid(row=0, column=2, sticky='W')
blue_slider.grid(row=1, column=2, sticky='W')
blue_button.grid(row=2, column=2, padx=1, pady=1, ipadx=14)

# Create buttons for each complimentary color

yellow_button = tkinter.Button(input_frame, text="Yellow", command=lambda: set_color(250, 250, 0))
cyan_button = tkinter.Button(input_frame, text="Cyan", command=lambda: set_color(0, 250, 250))
magenta_button = tkinter.Button(input_frame, text="Magenta", command=lambda: set_color(250, 0, 250))

yellow_button.grid(row=3, column=0, padx=1, pady=1, sticky="WE")
cyan_button.grid(row=3, column=1, padx=1, pady=1, sticky="WE")
magenta_button.grid(row=3, column=2, padx=1, pady=1, sticky="WE")

# Create utility buttons
store_button = tkinter.Button(input_frame, text="Store Color", command=store_color)
save_button = tkinter.Button(input_frame, text="Save", command=save)
quit_button = tkinter.Button(input_frame, text="Quit", command=root.destroy)

store_button.grid(row=4, column=0, columnspan=3, padx=1, pady=1, sticky="WE")
save_button.grid(row=4, column=3, padx=1, pady=1, sticky="WE")
quit_button.grid(row=4, column=4, padx=1, pady=1, sticky="WE")

# Create the color box and color labels
color_black_box = tkinter.Label(input_frame, bg='black', height=5, width=12)
color_box = tkinter.Label(input_frame, bg='black', height=5, width=12)
color_tuple = tkinter.Label(input_frame, text='(0), (0), (0)')
color_hex = tkinter.Label(input_frame, text='#000000')

color_black_box.grid(row=1, column=3, columnspan=2, padx=25, pady=5, ipadx=10, ipady=10)
color_box.grid(row=1, column=3, columnspan=2, padx=25, pady=5, ipadx=5, ipady=5)
color_tuple.grid(row=2, column=3, columnspan=2)
color_hex.grid(row=3, column=3, columnspan=2)

colors = {}
color = IntVar()

# Create radio buttons to select stored colors and populate each row with placeholder values
for x in range(6):
    radio = tkinter.Radiobutton(output_frame, variable=color, value=x)
    radio.grid(row=x, column=0, sticky="WE")

    recall_button = tkinter.Button(output_frame, text="Recall Color")
    recall_button.grid(row=x, column=1, padx=10, pady=1)

    new_color_tuple = tkinter.Label(output_frame, text="(255) (255) (255)")
    new_color_tuple.grid(row=x, column=2, padx=10, pady=1)

    new_color_hex = tkinter.Label(output_frame, text="#ffffff")
    new_color_hex.grid(row=x, column=3, padx=10, pady=1)

    new_color_black_box = tkinter.Label(output_frame, bg="black", height=1, width=3)
    new_color_black_box.grid(row=x, column=4, padx=10, pady=1, ipadx=5, ipady=5)

    new_color_box = tkinter.Label(output_frame, bg="white", height=1, width=3)
    new_color_box.grid(row=x, column=4, pady=1, ipadx=1, ipady=1)

    colors[color.get()] = [new_color_tuple.cget('text'), new_color_hex.cget('text')]
# Call root window's main loop
root.mainloop()

