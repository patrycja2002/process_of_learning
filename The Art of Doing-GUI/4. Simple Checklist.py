# Simple Checklist
import tkinter
from tkinter import END, ANCHOR

# Define window
root = tkinter.Tk()
root.title("Simple Checklist")
root.geometry("500x500")
root.resizable(0, 0)

# Define fonts and colors
my_font = ('Times New Roman', 12)
root_color = "#880e4f"
button_color = "#E084A3"
root.config(bg=root_color)


# Define functions
def add_item():
    """Add an individual item to the listbox"""
    my_listbox.insert(END, list_entry.get())
    list_entry.delete(0, END)


def remove_item():
    """Remove the selected (ANCHOR) item from the listbox"""
    my_listbox.delete(ANCHOR)


def clear_list():
    """Delete all items from the listbox"""
    my_listbox.delete(0, END)


def save_list():
    """Save the list to a simple txt file"""
    with open("checklist.txt", "w") as f:
        list_tuple = my_listbox.get(0, END)
        for item in list_tuple:
            # Take proper precautions to include only one \n for formatting purposes
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item + "\n")


def open_list():
    """Open the list upon starting the program if there is one"""
    try:
        with open("checklist.txt", "r") as f:
            for line in f:
                my_listbox.insert(END, line)
    except:
        return


# Define layout
# Create frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

# Input frame layout
list_entry = tkinter.Entry(input_frame, width=40, borderwidth=3)
list_add_button = tkinter.Button(input_frame, text="Add Item", width=10, font=my_font, bg=button_color,
                                 command=add_item)
list_entry.grid(row=0, column=0, padx=10, pady=10)
list_add_button.grid(row=0, column=1, padx=10, pady=10)

# Output frame layout
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, height=19, width=55, borderwidth=4, font=my_font,
                             yscrollcommand=my_scrollbar.set)

# Link scrollbar to listbox
my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

# Button Frame layout
list_remove_button = tkinter.Button(button_frame, text="Remove Item", width=10, font=my_font, bg=button_color,
                                    command=remove_item)
list_clear_button = tkinter.Button(button_frame, text="Clear List", width=10, font=my_font, bg=button_color,
                                   command=clear_list)
list_save_button = tkinter.Button(button_frame, text="Save List", width=10, font=my_font, bg=button_color,
                                  command=save_list)
quit_button = tkinter.Button(button_frame, text="Quit", width=10, font=my_font, bg=button_color, command=root.destroy)

list_remove_button.grid(row=1, column=0, padx=2, pady=10)
list_clear_button.grid(row=1, column=1, padx=2, pady=10, ipadx=10)
list_save_button.grid(row=1, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=1, column=3, padx=2, pady=10)

# Open the previous list if available
open_list()

# Call root window's main loop
root.mainloop()
