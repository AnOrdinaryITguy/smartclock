import requests
import json
from settings import Settings

# A list for storing the weather to reduce the amount of API calls.
WeatherStoringList = []

SLStoringList = []


class WeatherData:
    """A class for storing the weather reports variables"""
    def __init__(self, validtime, temperature, forecast):
        self.validtime = validtime
        self.temperature = temperature
        self.forecast = forecast


class SLData:
    """A class for storing the SL reports variables"""
    def __init__(self, direction, displaytime):
        self.direction = direction
        self.displaytime = displaytime


class GeneralUpdates:
    """A class for storing updates relating to weather and traffic"""
    def UpdateWeather():
        settings = Settings()
        """A function for getting and formatting the weather for the coming week"""
        #print("Running Weather Function")
        GetWeatherReport = requests.get('https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/'+settings.weather_lon+'/lat/'+settings.weather_lat+'/data.json')
        GetWeatherJSON = json.loads(GetWeatherReport.text)
        WeatherDictionary={
            1: 'Clear sky',
            2: 'Nearly clear sky',
            3: 'Variable cloudiness',
            4: 'Halfclear sky',
            5:'Cloudy sky',
            6: 'Overcast',
            7: 'Fog',
            8: 'Light rain showers',
            9: 'Moderate rain showers',
            10: 'Heavy rain showers',
            11: 'Thunderstorm',
            12: 'Light sleet showers',
            13: 'Moderate sleet showers',
            14: 'Heavy sleet showers',
            15: 'Light snow showers',
            16: 'Moderate snow showers',
            17: 'Heavy snow showers',
            18: 'Light rain',
            19: 'Moderate rain',
            20: 'Heavy rain',
            21: 'Thunder',
            22: 'Light sleet',
            23: 'Moderate sleet',
            24: 'Heavy sleet',
            25: 'Light snowfall',
            26: 'Moderate snowfall',
            27: 'Heavy snowfall'
            }
    
        # Clear the list before adding new data to it.
        WeatherStoringList.clear()
        # Loop through the reports in the JSON blob
        for Weatherreports in GetWeatherJSON['timeSeries']:
            # Get the valid time of the current weatherreport
            WeatherReportValidTime=(str(Weatherreports['validTime']))
            # Get the temperature(Celcius) of the current weatherreport
            WeatherTemperature = str(Weatherreports['parameters'][10]['values']).strip("[]")
            # Get the actual Weather using the dictionary created before.
            WeatherMeaning = str(WeatherDictionary.get(Weatherreports['parameters'][18]['values'][0]))
        
            WeatherStoringList.append(WeatherData(validtime = WeatherReportValidTime,temperature = WeatherTemperature,forecast = WeatherMeaning))
            #WeatherStoringList.append(Reporteddata)

    def UpdateSLtimetables():
        settings = Settings()
        GetSLStatus = requests.get('https://transport.integration.sl.se/v1/sites/'+settings.station_id+'/departures') #Gets 10 min of arrivals

        GetSLStatusJSON = json.loads(GetSLStatus.text)
        #print(GetSLStatusJSON)
        SLStoringList.clear()
        for JSONObjects in GetSLStatusJSON['departures']:
            #print(JSONObjects)
            if str(JSONObjects['line']['transport_mode']) == 'METRO':
                #Clear the list before adding new fresh data into it
                SLStoringList.append(SLData(direction=str(JSONObjects['direction']), displaytime=str(JSONObjects['display'])))

#GeneralUpdates.UpdateWeather()
#print(WeatherStoringList[0].validtime)
#print(WeatherStoringList[0].temperature)
#print(WeatherStoringList[0].forecast)

#GeneralUpdates.UpdateSLtimetables()
#print(SLStoringList[0].direction)
#print(SLStoringList[0].displaytime)