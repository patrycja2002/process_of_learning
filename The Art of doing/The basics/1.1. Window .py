# Window Basics
import tkinter
# Define window
root = tkinter.Tk()
root.title("Window basics")
root.geometry("250x700")
root.resizable(0, 0)
root.config(bg="blue")

# Second window
top = tkinter.Toplevel()
top.title("Second window")
top.config(bg="#123456")
top.geometry("200x200+500+50")

# Run root window's main loop
root.mainloop()

