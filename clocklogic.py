import statusupdates

from datetime import datetime, timedelta
from time import strftime

currentweather = [""]

class ClockWidget():
    """Some logic to display the time and keep track of which api calls should be done."""

    def IntitialStart():
        # Update the list at the first start of the clock.
        statusupdates.GeneralUpdates.UpdateSLtimetables()
        statusupdates.GeneralUpdates.UpdateWeather()
        for timeslot in statusupdates.WeatherStoringList:
            if timeslot.validtime != "null":
                WeatherReportTime = datetime.strftime(datetime.strptime(timeslot.validtime, '%Y-%m-%dT%H:%M:%SZ'),'%Y-%m-%d hour: %H')
                
                CurrentTime = strftime('%Y-%m-%d hour: %H')
                OneDay = (datetime.now() + timedelta(hours=24)).strftime('%Y-%m-%d hour: %H')
                TwoDay = (datetime.now() + timedelta(hours=48)).strftime('%Y-%m-%d hour: 12')

                if WeatherReportTime in (CurrentTime, OneDay, TwoDay):
                    currentweather.append(str(datetime.strftime(datetime.strptime(timeslot.validtime, '%Y-%m-%dT%H:%M:%SZ'),'%A'))+"\n-"+str(timeslot.forecast)+", "+str(timeslot.temperature)+ " °C")

            else:
                currentweather.clear()
                currentweather.append(str(timeslot.forecast)+"\n-"+str(timeslot.temperature)+ " °C")

    def CurrentTime():
        DayOfTheWeek = strftime('%A')
        #Checks for the APIs
        ClockWidget.TimeChecks()
        #ClockWidget.DayChecks()
        GetCurrentTime = strftime('%H:%M')
        DayOfTheWeek = strftime('%A')

        # Added a clock filter for the night:
        if 0 <= int(strftime('%-H')) <= 8:
            if strftime('%A') == "Saturday" or strftime('%A') == "Sunday":
                return '--:--'+"\n"+str(DayOfTheWeek)+"\nIt's Weekend!"
            else:
                return '--:--'+"\n"+str(DayOfTheWeek)+"\nIt's workday:("
        else:
            if strftime('%A') == "Saturday" or strftime('%A') == "Sunday":
                return str(GetCurrentTime)+"\n"+str(DayOfTheWeek)+"\nIt's Weekend!"
            else:
                return str(GetCurrentTime)+"\n"+str(DayOfTheWeek)+"\nIt's workday:("

    def CurrentYear():
        CurrentDate = strftime('%-d %B %Y')
        return CurrentDate

    def TimeChecks():
        EveryHourCheck = strftime('%M:%S')
        EveryMinuteCheck = strftime('%S')
        if EveryHourCheck == '00:10':
            currentweather.clear() # Current fix to avoid filling the list with shit.
            for timeslot in statusupdates.WeatherStoringList:
                if timeslot.validtime != "null":
                    WeatherReportTime = datetime.strftime(datetime.strptime(timeslot.validtime, '%Y-%m-%dT%H:%M:%SZ'),'%Y-%m-%d hour: %H')
                    
                    CurrentTime = strftime('%Y-%m-%d hour: %H')
                    OneDay = (datetime.now() + timedelta(hours=24)).strftime('%Y-%m-%d hour: %H')
                    TwoDay = (datetime.now() + timedelta(hours=48)).strftime('%Y-%m-%d hour: 12')
                    currentweather.clear()

                    if WeatherReportTime in (CurrentTime, OneDay, TwoDay):
                        currentweather.append(str(datetime.strftime(datetime.strptime(timeslot.validtime, '%Y-%m-%dT%H:%M:%SZ'),'%A'))+"\n-"+str(timeslot.forecast)+", "+str(timeslot.temperature)+ " °C")
                    else:
                        # This might cause a bug..
                        currentweather.clear()
                        # If no weather matching the current time is find update the list with new times and run the function again.
                        statusupdates.GeneralUpdates.UpdateWeather()
                        ClockWidget.TimeChecks()
                else:
                    currentweather.append(str(timeslot.forecast)+"\n-"+str(timeslot.temperature)+ " °C")

        if EveryMinuteCheck == '00':
            statusupdates.GeneralUpdates.UpdateSLtimetables()
            #print("Updating Stored SL Data")
        ClockWidget.CurrentTime.Weekend_check = True

