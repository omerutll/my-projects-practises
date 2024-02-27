import requests

API_KEY = '538fac11f82e1c4a93ad00b7a8ce3d54'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('enter a city name: ') 
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
  data =  response.json()
  weather = data['weather'][0]['description']
  temp = (data['main']['temp']-273)
  temp_rounded = round(temp, 1)
  print(f'the weather is {weather} and temperature is {temp_rounded} C yunus gay')
else:
  print('an error occured')