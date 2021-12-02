# APOD Viewer
import tkinter, requests, webbrowser
from tkinter import filedialog
from tkcalendar import DateEntry
from PIL import ImageTk, Image
from io import BytesIO

# Define window
root = tkinter.Tk()
root.title("APOD Viewer")

# Define fonts and colors
text_font = ('Times New Roman', 14)
nasa_blue = "#043c93"
nasa_light_blue = "#7aa5d3"
nasa_red = "#ff1923"
nasa_white = "#ffffff"
root.config(bg=nasa_blue)


# Define functions
def get_request():
    global response
    url = 'https://api.nasa.gov/planetary/apod'
    api_key = 'DEMO_KEY'
    date = calander.get_date()
    querystring = {'api_key': api_key, 'date': date}
    response = requests.request("GET", url, params=querystring)
    response = response.json()
    set_data()
    print(response)


def set_data():
    # Example response
    """{'copyright': 'Dietmar Hager', 'date': '2021-12-02', 'explanation': "Grand spiral galaxies often seem to get all
    the glory, flaunting their young, bright, blue star clusters in beautiful, symmetric spiral arms. But small
    galaxies form stars too, like nearby NGC 6822, also known as Barnard's Galaxy. Beyond the rich starfields in the
    constellation Sagittarius, NGC 6822 is a mere 1.5 million light-years away, a member of our Local Group of
    galaxies. A dwarf irregular galaxy similar to the Small Magellanic Cloud, NGC 6822 is about 7,000 light-years
    across. Brighter foreground stars in our Milky Way have a spiky appearance. Behind them, Barnard's Galaxy is seen to
    be filled with young blue stars and mottled with the telltale pinkish hydrogen glow of star forming regions in
    this deep color composite image.", 'hdurl': 'https://apod.nasa.gov/apod/image/2112/NGC6822LRGB-1.jpg', 'media_type':
    'image', 'service_version': 'v1', 'title': "NGC 6822: Barnard's Galaxy",
    'url': 'https://apod.nasa.gov/apod/image/2112/NGC6822LRGB-11024.jpg'} """

    explanation = response["explanation"]
    date = response["date"]

    picture_explanation.config(text=explanation)
    picture_date.config(text=date)
    get_photo()


def get_photo():
    global img
    global thumb
    global full_img
    url = response["url"]
    type = response["media_type"]
    if type == "image":
        photo_request = requests.get(url, stream=True)
        data_picture = photo_request.content
        img = Image.open(BytesIO(data_picture))
        full_img = ImageTk.PhotoImage(img)

        thumb_data = photo_request.content
        thumb = Image.open(BytesIO(thumb_data))
        thumb.thumbnail((200, 200))
        thumb = ImageTk.PhotoImage(thumb)
        picture_label.config(image=thumb)
    elif type == "video":
        picture_label.config(text=url)
        webbrowser.open(url)


def full():
    root_picture = tkinter.Toplevel()
    root_picture.title("Full APOD Viewer")

    label_picture = tkinter.Label(root_picture, image=full_img)
    label_picture.pack()


def save():
    save_name = filedialog.asksaveasfilename(initialdir='./', title='Save Image',
                                             filetypes=(('JPEG', '.jpg'), ('All Files', '*.*')))
    img.save(save_name)


# Define layout
# Create frames
input_frame = tkinter.Frame(root, bg=nasa_blue)
output_frame = tkinter.Frame(root, bg=nasa_white)
input_frame.pack()
output_frame.pack(padx=50, pady=(0, 25))

# Layout for the input frame
calander = DateEntry(input_frame, width=10, font=text_font, background=nasa_blue, foreground=nasa_white)
submit_button = tkinter.Button(input_frame, text="Submit", font=text_font, bg=nasa_light_blue, command=get_request)
full_button = tkinter.Button(input_frame, text="Full Photo", font=text_font, bg=nasa_light_blue, command=full)
save_button = tkinter.Button(input_frame, text="Save Photo", font=text_font, bg=nasa_light_blue, command=save)
quit_button = tkinter.Button(input_frame, text="Exit", font=text_font, bg=nasa_red, command=root.destroy)
calander.grid(row=0, column=0, padx=5, pady=10)
submit_button.grid(row=0, column=1, padx=5, pady=10, ipadx=35)
full_button.grid(row=0, column=2, padx=5, pady=10, ipadx=25)
save_button.grid(row=0, column=3, padx=5, pady=10, ipadx=25)
quit_button.grid(row=0, column=4, padx=5, pady=10, ipadx=50)

# Layout for the output frame
picture_date = tkinter.Label(output_frame, font=text_font, bg=nasa_white)
picture_explanation = tkinter.Label(output_frame, font=text_font, bg=nasa_white, wraplength=600)
picture_label = tkinter.Label(output_frame)
picture_date.grid(row=1, column=1, padx=10)
picture_explanation.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
picture_label.grid(row=0, column=1, padx=10, pady=10)

# Get today's photo to start with
get_request()

# Call root window's main loop
root.mainloop()
