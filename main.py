from tkinter import *

import requests


root = Tk()

root.title('Weather app')
root.geometry('400x300+550+100')
root.resizable(True,True)
root.config(bg='#beeaec')
# icon = PhotoImage(file='logo.png')
# root.iconphoto(False, icon)


# create a labels and set fornts
title_label = Label(root, text='Weather App', font=('Arial', 20), bg='#2E4053', fg='white')
title_label.pack(side=TOP, fill=X, padx=10, )



location_label = Label(root, text='Location', font=('Arial', 12), bg='#2E4053', fg='white')
location_label.pack(pady=10)


# Entry widget for loaction input
location_entry = Entry(root, font=('Arial', 12))
location_entry.pack(pady=5)


# city_name = 'Bhubaneswar'
#API_key = '1cddee7d76a60a7b2291337b5ada52dd'
#url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'


# Function to update weather date (dummy date for demonstration)
def get_weather():
    city_name = location_entry.get()

    API_key = '1cddee7d76a60a7b2291337b5ada52dd'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

    print(city_name)
    response =requests.get(url)

    if response.status_code == 200:     # meaning of 200 is url successfully runed, and we get result.
        data = response.json()

        Condition = str(data['weather'][0]['description'])
        temp = str(data['main']['temp'])
        humidity = str(data['main']['humidity'])
        wind_speed = str(data['wind']['speed']) 

    text_ = 'Temperature: '+ temp +"°C\nCondition: "+ Condition + "\nHumidity: " + humidity + "\nWind Speed: " + wind_speed 
    weather_data.config(text= text_)

# Button to get weather
get_weather_button = Button(root, text='Get Weather', command=get_weather, font=('Arial', 12), bg='#FF5733', fg='white')
get_weather_button.pack(pady=10)



# Frame to display weather information
weather_frame = LabelFrame(root, text='Weather Info', labelanchor='n')
weather_frame.pack(padx=10, pady=10, fill='both', expand='yes')



# Labels to display weather data
weather_data = Label(weather_frame, text='Temperature: 25°C\nCondition: Sunny', font=('Arial', 12), bg='#FFC300')
weather_data.pack(padx=10, pady=10)



root.mainloop()