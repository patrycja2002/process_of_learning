# Weather Forecast
import requests
import tkinter
from tkinter import BOTH, IntVar
from PIL import ImageTk, Image
from io import BytesIO

# Define window
root = tkinter.Tk()
root.title("Gravity Simulation")
root.geometry("400x420")
root.resizable(0, 0)

# Define fonts and colors
sky_color = "#4fc3f7"
grass_color = "#00c853"
output_color = "#b3e5fc"
input_color = "#c8e6c9"
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)


# Define functions
def search_():
    global response
    # Get API response
    # URL and my api key, Use your own api key
    url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "4bc709494b4867d661ab188903863182"
    # Search by the appropriate query, either city name or zip
    if search.get() == 1:
        querystring = {"q": city_entry.get(), "appid": api_key}
    elif search.get() == 2:
        querystring = {"id": city_entry.get(), "appid": api_key}

    response = requests.request("GET", url, params=querystring)
    response = response.json()
    get_weather()
    get_icon()
    print(response)

def get_weather():
    # Gather the data to be used from the API response
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']["lon"])
    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']
    temp = str(response["main"]["temp"])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    city_info_label.config(text=city_name + "(" + city_lat + ", " + city_lon + ")", font=large_font, bg=output_color)
    weather_label.config(text="Weather: " + main_weather + ", " + description, font=small_font, bg=output_color)
    temp_label.config(text='Temperature: ' + temp + " F", font=small_font, bg=output_color)
    feels_label.config(text="Feels Like: " + feels_like + " F", font=small_font, bg=output_color)
    temp_min_label.config(text="Min Temperature: " + temp_min + " F", font=small_font, bg=output_color)
    temp_max_label.config(text="Max Temperature: " + temp_max + " F", font=small_font, bg=output_color)
    humidity_label.config(text="Humidity: " + humidity, font=small_font, bg=output_color)


def get_icon():
    global img
    # Get the icon id from API response.
    icon_id = response['weather'][0]['icon']
    # Get the icon from the correct website
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

    # Make a request at the url to download the icon; stream=True automatically dl
    icon_response = requests.get(url, stream=True)
    # Turn into a form tkinter/python can use
    img_data = icon_response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    # Update label
    photo_label.config(image=img)

# Define layout
# Create frames
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=325, height=235)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

# Layout for the output frame
city_info_label = tkinter.Label(output_frame, bg=output_color)
weather_label = tkinter.Label(output_frame, bg=output_color)
temp_label = tkinter.Label(output_frame, bg=output_color)
feels_label = tkinter.Label(output_frame, bg=output_color)
temp_min_label = tkinter.Label(output_frame, bg=output_color)
temp_max_label = tkinter.Label(output_frame, bg=output_color)
humidity_label = tkinter.Label(output_frame, bg=output_color)
photo_label = tkinter.Label(output_frame, bg=output_color)

city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack()

# Layout for the input frame
city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(input_frame, text='Submit', font=large_font, bg=input_color, command=search_)
search = IntVar()
search.set(1)
search_city = tkinter.Radiobutton(input_frame, text='Search by city name', variable=search, value=1, font=small_font, bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text="Search by zipcode", variable=search, value=2, font=small_font, bg=input_color)
city_entry.grid(row=0, column=0, padx=10, pady=(10, 0))
submit_button.grid(row=0, column=1, padx=10, pady=(10, 0))
search_city.grid(row=1, column=0, pady=2)
search_zip.grid(row=1, column=1, padx=5, pady=2)

# Call root window's main loop
root.mainloop()
