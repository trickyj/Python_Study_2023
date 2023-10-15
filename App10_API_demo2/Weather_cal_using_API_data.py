import requests
city = 'pune'
#We are going to defin the json data url and fetch the same and print it.
url = 'http://api.weatherapi.com/v1/current.json?key=ddc430336fc4403091461127231510&q='+city+'&aqi=no'
response = requests.get(url)
#here we are writing the new variable called weather_json and capturing the data from the above response variable in JSON format.
weather_json = response.json()
# this will print all the data from the weather api json file and we want specific keys from the dictionary.
#print(weather_json)
#basically we want to know only the current temperature in cencius.
temp = weather_json.get('current').get('temp_c')
description = weather_json.get('current').get('condition').get('text')
print('\ntodays weather in', city, 'is', description, 'and', temp, 'degrees\n')