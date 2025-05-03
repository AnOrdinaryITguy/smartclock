import statusupdates

from datetime import datetime
from time import strftime

currentweather = ["Unkown"]

class ClockWidget():
    """Some logic to display the time and keep track of which api calls should be done."""

    def IntitialStart():
        # Update the list at the first start of the clock.
        statusupdates.GeneralUpdates.UpdateSLtimetables()
        statusupdates.GeneralUpdates.UpdateWeather()
        for timeslot in statusupdates.WeatherStoringList:
            if timeslot.validtime != "null":
                if strftime('%Y-%m-%d hour: %H') == datetime.strftime(datetime.strptime(timeslot.validtime, '%Y-%m-%dT%H:%M:%SZ'),'%Y-%m-%d hour: %H'):
                    currentweather.clear()
                    currentweather.append(str(timeslot.forecast)+", "+str(timeslot.temperature)+ " °C")
            else:
                currentweather.clear()
                currentweather.append(str(timeslot.forecast)+", "+str(timeslot.temperature)+ " °C")

    def CurrentTime():
        DayOfTheWeek = strftime('%A')
        #Checks for the APIs
        ClockWidget.TimeChecks()
        #ClockWidget.DayChecks()
        # Added a clock filter for the night:
        if 0 <= int(strftime('%-H')) <= 8:
            GetCurrentTime = '--:--'
        else:
            GetCurrentTime = strftime('%H:%M')

        if strftime('%A') == "Saturday" or strftime('%A') == "Sunday":
            return str(DayOfTheWeek)+" "+str(GetCurrentTime)+"\nIt's Weekend!"
        else:
            return str(DayOfTheWeek)+" "+str(GetCurrentTime)+"\nIt's workday:("

    def CurrentYear():
        CurrentDate = strftime('%-d %B %Y')
        return CurrentDate

    def TimeChecks():
        EveryHourCheck = strftime('%M:%S')
        EveryMinuteCheck = strftime('%S')
        if EveryHourCheck == '00:10':
            for timeslot in statusupdates.WeatherStoringList:
            # checks if the date and report is equal to the weather reports date and time
                if timeslot.validtime != "null":
                    if strftime('%Y-%m-%d hour: %H') == datetime.strftime(datetime.strptime(timeslot.validtime, '%Y-%m-%dT%H:%M:%SZ'),'%Y-%m-%d hour: %H'):
                        currentweather.clear()
                        currentweather.append(str(timeslot.forecast)+", "+str(timeslot.temperature)+ " °C")
                    else:
                        # If no weather matching the current time is find update the list with new times and run the function again.
                        statusupdates.GeneralUpdates.UpdateWeather()
                        ClockWidget.TimeChecks()
                else:
                    currentweather.clear()
                    currentweather.append(str(timeslot.forecast)+", "+str(timeslot.temperature)+ " °C")

        if EveryMinuteCheck == '00':
            statusupdates.GeneralUpdates.UpdateSLtimetables()
            #print("Updating Stored SL Data")
        ClockWidget.CurrentTime.Weekend_check = True

