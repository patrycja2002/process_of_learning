# Images
import tkinter
from PIL import ImageTk, Image

# Define window
root = tkinter.Tk()
root.title("Image Basics!")
root.geometry("700x700")
root.resizable(0, 0)


# Define functions
def make_image():
    '''Print an image'''
    global flower_image
    # Using PIL for jpg
    flower_image = ImageTk.PhotoImage(Image.open("flower.jpg"))
    flower_label = tkinter.Label(root, image=flower_image)
    flower_label.pack()

# Basics...works for png
my_image = tkinter.PhotoImage(file="shield.png")
my_label = tkinter.Label(root, image=my_image)
my_label.pack()

my_button = tkinter.Button(root, image=my_image)
my_button.pack()

# Not for jpeg
# flower_image = tkinter.PhotoImage(file="flower.jpg")
# flower_label = tkinter.Label(root, image=flower_image)
# flower_label.pack()

make_image()

# Call root window's main loop
root.mainloop()
