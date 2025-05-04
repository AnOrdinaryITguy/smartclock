from art import *
import clocklogic
import os
import statusupdates
from settings import Settings
import time

settings = Settings()


clocklogic.ClockWidget.IntitialStart()

savedtime=clocklogic.ClockWidget.CurrentTime()

os.system('cls' if os.name == 'nt' else 'clear')
tprint(clocklogic.ClockWidget.CurrentTime(),font=settings.main_clock_font,chr_ignore=True) # print ASCII text (block font)
tprint(clocklogic.ClockWidget.CurrentYear(),font=settings.main_clock_font,chr_ignore=True) # print ASCII text (block font)



while True:
    if savedtime != clocklogic.ClockWidget.CurrentTime():
        os.system('cls' if os.name == 'nt' else 'clear')
        tprint(clocklogic.ClockWidget.CurrentTime(),font=settings.main_clock_font,chr_ignore=True) # print ASCII text (block font)
        tprint(clocklogic.ClockWidget.CurrentYear(),font=settings.main_clock_font,chr_ignore=True) # print ASCII text (block font)
        # Wait 15 seconds until next section.
        time.sleep(15)
        # Clear the screen for the next section.
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the weather
        tprint("Weather",font=settings.main_clock_font,chr_ignore=True) # print ASCII text (block font)
        for WeatherReports in clocklogic.currentweather: 
            tprint(WeatherReports, font=settings.sub_clock_font,chr_ignore=True)
        # Wait 15 seconds until next section.
        time.sleep(15)
        # Clear the screen for the next section.
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print the train times    
        tprint("Metro",font=settings.main_clock_font,chr_ignore=True) # print ASCII text (block font)
        for update in statusupdates.SLStoringList:
            tprint(str(update.direction)+" "+str(update.displaytime), font=settings.sub_clock_font,chr_ignore=True)
        time.sleep(15)
        savedtime=clocklogic.ClockWidget.CurrentTime()
        continue
