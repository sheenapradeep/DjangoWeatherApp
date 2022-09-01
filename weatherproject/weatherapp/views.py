from urllib.error import HTTPError, URLError
from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
from .models import City

def index(request):
    ## importing the data from database
    cities = City.objects.all() 
    ## All the objects from the database is returned to be viewed from the template. 
    data = {'info': cities}   
  

    if request.method == 'POST':
        input = str(request.POST['state'])
        input = input.split(",")

   
        city = "{" + input[0].replace(" ","+") + "}"

        if len(input) == 3:
            state = "{" + input[1].replace(" ","+") + "}"
            country = "{" + input[2].replace(" ","+") + "}"
        if len(input) == 2:
            state = '{NA}'
            country = "{" + input[1].replace(" ","+") + "}"

        ## If state is not provided, then the url should only have the city and country, if not then it should include the state. 
        if state == '{NA}':
            url = 'http://api.openweathermap.org/geo/1.0/direct?q={},{}&appid=yourAPIKEY'.format(city,country)
            print(url)
            urlGetCoordinates = urllib.request.urlopen(url)
            urlGetCoordinates = urlGetCoordinates.read()       
        else:
            url = 'http://api.openweathermap.org/geo/1.0/direct?q={},{},{}&appid=yourAPIKEY'.format(city,state,country)
            print(url)
            urlGetCoordinates = urllib.request.urlopen(url)
            urlGetCoordinates = urlGetCoordinates.read()



        datalist = json.loads(urlGetCoordinates)
        dataCoordinates = {
            'lat': str(datalist[0]['lat']),
            'lon' : str(datalist[0]['lon'])  
        }

        # Get the weather information from the lat and long that user requests and return results page with data
        urlWeather = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid=yourAPIKEY'.format(dataCoordinates['lat'],dataCoordinates['lon'])).read()
        urlWeatherlist = json.loads(urlWeather)


        data = {
            'name': str(urlWeatherlist['name']),
            'weather': str(urlWeatherlist['weather'][0]['main']),
            'description': str(urlWeatherlist['weather'][0]['description']).title(),
            'icon': str(urlWeatherlist['weather'][0]['icon']),
            'temp': str(urlWeatherlist['main']['temp']),
            'feelslike': str(urlWeatherlist['main']['feels_like'])
        }
            
            
        return render(request,'results.html', data)
       


    return render(request,'weather.html', data)