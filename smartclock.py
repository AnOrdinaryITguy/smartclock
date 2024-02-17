import tkinter as tk
from time import strftime
import requests
import json
from datetime import datetime
import time

class StatusWindowGUI:
        def __init__(self):
                #RootWindow
                self.RootWindow = tk.Tk()
                self.RootWindow.geometry("1024x600")
                self.RootWindow.configure(bg='#26282a')
                #self.RootWindow.attributes('-fullscreen', True)                
                #Clock Section
                def ClockWidget():
                        self.GetCurrentTime = strftime('%H:%M')
                        self.TimeLabel.config( text= self.GetCurrentTime)
                        #add day of the week after this section!
                        self.DayOfTheWeek = strftime('%A')
                        self.DayLabel.config(text= self.DayOfTheWeek)
                        self.EveryHourCheck = strftime('%M:%S')
                        self.EveryMinuteCheck = strftime('%S')
                        def GetWeather():
                                print("Running Weather Function")
                                GetWeather = requests.get('https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/123/lat/123/data.json') #Change longitude att latitude to match desired location
                                GetWeatherJSON = json.loads(GetWeather.text)

                                WeatherTimeList = []
                                WeatherTemperatureList = []
                                WeatherSummaryList = []
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
                                JSONdocamount=0
                                for JSONdocument in GetWeatherJSON['timeSeries']:
                                        
                                        pretime=(str(JSONdocument['validTime']))
                                        #adds the forecast Date
                                        WeatherTimeList.append(datetime.strftime(datetime.strptime(pretime, '%Y-%m-%dT%H:%M:%SZ'),'%A'))
                                        #adds the temperature
                                        WeatherTemperatureList.append(str(JSONdocument['parameters'][10]['values']).strip("[]"))
                                        #adds the weatherforecast
                                        WeatherSymbol = WeatherDictionary.get(GetWeatherJSON['timeSeries'][JSONdocamount]['parameters'][18]['values'][0])
                                        
                                        #adds all values to a summary list
                                        WeatherSummaryList.append(str(WeatherTimeList[JSONdocamount])+", "+str(WeatherSymbol)+", "+str(WeatherTemperatureList[JSONdocamount])+" °C")
                                        #counts the JSONdocument with JSONdocamount
                                        JSONdocamount+=1
                                MaxJson = JSONdocamount-1
                                self.WeatherLabel.config(text=(WeatherSummaryList[2]+"\n"+WeatherSummaryList[26]+"\n"+WeatherSummaryList[50]+"\n"+WeatherSummaryList[MaxJson]))
                                
                       #SL check
                        def SLcheck():
                            print("Running SL Function")
                            SLAPIkey = 'INPUT API KEY HERE'
                            SiteID = 'INPUT SITE ID HERE'
                            GetSLStatus = requests.get('https://api.sl.se/api2/realtimedeparturesV4.json?key='+SLAPIkey+'&siteid='+SiteID+'&timewindow=30') #Gets 10 min of arrivals
                            GetSLStatusJSON = json.loads(GetSLStatus.text)
                            SLDeparturelist = []
                            for JSONObjects in GetSLStatusJSON['ResponseData']['Metros']:
                                SLDeparturelist.append(JSONObjects['DisplayTime']+" "+JSONObjects['Destination'])
                            self.SLDepartureLabel.config(text=(SLDeparturelist[0]+"\n"+SLDeparturelist[1]+"\n"+SLDeparturelist[2]+"\n"+SLDeparturelist[3]))
                        if self.EveryMinuteCheck == '00':
                            #SL timetable update
                            print("Minutecheck")
                            try:
                                print("Updating SL timetables")
                                SLcheck()
                                self.SLDepartureLabel.config(foreground='#f19615')
                            except:
                                print("Failed to update SL timetables")
                                self.SLDepartureLabel.config(text='Unable to retrieve SL timetables', foreground= 'red')
                        #Runs the weathercheck and daycheck everyhour
                        if self.EveryHourCheck == '00:10':
                            print("Hourcheck")
                            #Weather Update
                            try:
                                print("Updating Weather")
                                GetWeather()
                                self.WeatherLabel.config(foreground='#f19615')
                            except:
                                print("Weather update failed")
                                self.WeatherLabel.config(text='Unable to retrieve current weather', foreground= 'red')
                            #Day status update
                            if self.DayOfTheWeek == 'Saturday' or self.DayOfTheWeek == 'Sunday':
                                print("Checking Current day")
                                self.DayLabel.config(foreground= 'red')
                            else:
                                self.DayLabel.config(foreground= '#f19615')                       

                        self.DayLabel.after(1000, ClockWidget)#calls the function again.
                self.SwitchStatus = True
                def SwitchView():
                    if self.SwitchStatus == True:
                        print("Weather-view")
                        self.WeatherLabel.pack_forget()
                        self.SLDepartureLabel.pack_forget()
                        self.WeatherLabel.pack(padx=20, pady=0)
                        self.SwitchStatus = False
                    else:
                        print("Traffic-view")
                        self.WeatherLabel.pack_forget()
                        self.SLDepartureLabel.pack_forget()
                        self.SLDepartureLabel.pack(padx=20, pady=0)
                        self.SwitchStatus = True
                    
                #Day of the week
                self.DayLabel = tk.Label(self.RootWindow, font=('Helvetica',80), background='#26282a', foreground='#f19615')
                self.DayLabel.pack(padx=20, pady=20)
                #Clock
                self.TimeLabel = tk.Label(self.RootWindow, font=('Helvetica',80),background='#26282a', foreground='#f19615')
                self.TimeLabel.pack(padx=20, pady=20)
                #Button for switching between Traffic and Weather status
                self.SwitchViewButton = tk.Button(self.RootWindow, text ="Switch view", font=('Helvetica',30),background='#26282a', foreground='#f19615', activebackground='#26282a',activeforeground='#f19615',  borderwidth=3, relief="solid", command = SwitchView)
                self.SwitchViewButton.place(x=400, y=500)
                #Traffic label
                self.SLDepartureLabel = tk.Label(self.RootWindow, font=('Helvetica',30),background='#26282a', foreground='#f19615', text="Traffic-view", anchor="w", justify="left")
                self.SLDepartureLabel.pack(padx=20, pady=0)
                #Weather label
                self.WeatherLabel = tk.Label(self.RootWindow, font=('Helvetica',30),background='#26282a', foreground='#f19615', text="Weather-view",anchor="w", justify="left")
                

                ClockWidget()
                self.RootWindow.mainloop()

StatusWindowGUI()
