###******Collecting current weather forecast of cities using Python and Open Weather API*****###


import requests, json                                            ## importing request for HTTP requests and json for formatting the recieved data

api_key = "<YOUR API KEY>"                     ## api key obtained after signing up on open weather api

base_url = "http://api.openweathermap.org/data/2.5/weather?"     ## base request URL 
CITY = input("Enter city name : ")                               ## taking CITY name as input

complete_url = base_url + "appid=" + api_key + "&q=" + CITY      ## complete request URL

response = requests.get(complete_url)
if response.status_code == 200:                                  ##response code 200 suggests request has succeeded
   data = response.json()                                        ##getting data in the json format
                                                                
   main = data['main']
   
   temperature = int(main['temp'])                               ## fetching weather details in Dictionary
   humidity = main['humidity']
   pressure = main['pressure']
   report = data['weather']
   print(f"********{CITY}**********")
   temperature1 = round(temperature-273.15)
   print(f"Temperature(in C): {temperature1}")
   print(f"Humidity: {humidity} %")
   print(f"Pressure: {pressure} hPa")
   print(f"Weather Report: {report[0]['description']}")
else:
   print("Invalid Request!")