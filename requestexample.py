import requests
from bs4 import BeautifulSoup
import tkinter as tk

def get_weather(city):
    try:
        # creating url and requests instance
        url = "https://www.google.com/search?q=" + "weather" + city
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')

        # locating temperature and time
        temp = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
        time_and_sky = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text
        time, sky = map(str.strip, time_and_sky.split('\n', 1))

        # getting other required data
        details = soup.find('div', class_='BNeawe s3v9rd AP7Wnd').text

        # printing all data
        return temp, time, sky, details
    except Exception as e:
        return f"Error: {e}"

def update_weather():
    city_name = entry_city.get()
    temp, time, sky, details = get_weather(city_name)

    # Update labels with new weather data
    label_temp.config(text="Temperature is " + temp)
    label_time.config(text="Time: " + time)
    label_sky.config(text="Sky Description: " + sky)
    label_other_data.config(text=details)

# Create Tkinter window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
label_city = tk.Label(root, text="Enter City:")
label_city.grid(row=0, column=0, padx=10, pady=10)

entry_city = tk.Entry(root)
entry_city.grid(row=0, column=1, padx=10, pady=10)

button_get_weather = tk.Button(root, text="Get Weather", command=update_weather)
button_get_weather.grid(row=0, column=2, padx=10, pady=10)

label_temp = tk.Label(root, text="")
label_temp.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

label_time = tk.Label(root, text="")
label_time.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

label_sky = tk.Label(root, text="")
label_sky.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

label_other_data = tk.Label(root, text="")
label_other_data.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
