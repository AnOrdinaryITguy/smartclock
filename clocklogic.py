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
            if strftime('%Y-%m-%d hour: %H') == datetime.strftime(datetime.strptime(timeslot.validtime, '%Y-%m-%dT%H:%M:%SZ'),'%Y-%m-%d hour: %H'):
                currentweather.clear()
                currentweather.append(timeslot.forecast)


    def CurrentTime():
        GetCurrentTime = strftime('%H:%M')
        #add day of the week after this section!
        DayOfTheWeek = strftime('%A')

        #Checks for the APIs
        ClockWidget.TimeChecks()
        return GetCurrentTime
        
    def CurrentDay():
        #add day of the week after this section!
        DayOfTheWeek = strftime('%A')
        #Checks for the APIs
        ClockWidget.DayChecks()
        return DayOfTheWeek

    def CurrentYear():
        CurrentDate = strftime('%-d %B %Y')
        return CurrentDate

    def DayChecks():
        if strftime('%A') == "Saturday" or strftime('%A') == "Sunday":
            print("◕_◕ It's Weekend (◕ᴥ◕ʋ)")
        else:
            print("•`_´• It's a workday (╯°□°)╯︵ ┻━┻")


    def TimeChecks():
        EveryHourCheck = strftime('%M:%S')
        EveryMinuteCheck = strftime('%S')
        if EveryHourCheck == '00:10':
            for timeslot in statusupdates.WeatherStoringList:
            # checks if the date and report is equal to the weather reports date and time
                if strftime('%Y-%m-%d hour: %H') == datetime.strftime(datetime.strptime(timeslot.validtime, '%Y-%m-%dT%H:%M:%SZ'),'%Y-%m-%d hour: %H'):
                    currentweather.clear()
                    currentweather.append(timeslot.forecast)
                else:
                    # If no weather matching the current time is find update the list with new times and run the function again.
                    statusupdates.GeneralUpdates.UpdateWeather()
                    ClockWidget.TimeChecks()

        if EveryMinuteCheck == '00':
            statusupdates.GeneralUpdates.UpdateSLtimetables()
            #print("Updating Stored SL Data")

