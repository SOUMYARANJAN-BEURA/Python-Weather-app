import requests


city_name = 'Bhubaneswar'
API_key = '1cddee7d76a60a7b2291337b5ada52dd'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'   # this is used for geting temperature in celsious.

response =requests.get(url)

if response.status_code == 200:     # meaning of 200 is url successfully runed, and we get result.
    data = response.json()
    # print(data)
    print('Weather is ', data['weather'][0]['description'])
    print('Temperature is ', data['main']['temp'])
    print('Humidity is ', data['main']['humidity'])
    print('Wind speed is ', data['wind']['speed']) 