import requests

Cityname = 'Gujarat'
API_key = '5dcef99793d609477cfd5f336665b22d'
url = f'https://api.openweathermap.org/data/2.5/weather?q={Cityname}&appid={API_key}&units=metric'

respons = requests.get(url)
if respons.status_code == 200:
    data = respons.json()
    print('Weather is : ',data['weather'][0]['description'])
    print('Current tampurature is : ',data['main']['temp'])
    print('Current tampurature Feels like is : ',data['main']['feels_like'])
    
