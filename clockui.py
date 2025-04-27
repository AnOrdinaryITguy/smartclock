from art import *
import clocklogic
import os
import statusupdates
from settings import Settings


settings = Settings()


clocklogic.ClockWidget.IntitialStart()

savedtime=clocklogic.ClockWidget.CurrentTime()

tprint(clocklogic.ClockWidget.CurrentYear(),font=settings.mid_clock_font,chr_ignore=True) # print ASCII text (block font)
tprint(str(clocklogic.ClockWidget.CurrentDay())+'  '+str(clocklogic.ClockWidget.CurrentTime()),font=settings.main_clock_font,chr_ignore=True) # print ASCII text (block font)



while True:
    if savedtime != clocklogic.ClockWidget.CurrentTime():
        os.system('cls' if os.name == 'nt' else 'clear')
        tprint(clocklogic.ClockWidget.CurrentYear(),font=settings.mid_clock_font,chr_ignore=True) # print ASCII text (block font)
        tprint(str(clocklogic.ClockWidget.CurrentDay())+'  '+str(clocklogic.ClockWidget.CurrentTime()),font=settings.main_clock_font,chr_ignore=True) # print ASCII text (block font)
        # Print the weather
        print("\nToday's Weather:",clocklogic.currentweather[0])
       
        # Print the train times    
        tprint("Metro",font=settings.sub_clock_font,chr_ignore=True) # print ASCII text (block font)
        for update in statusupdates.SLStoringList:
            print(update.direction, update.displaytime)
        savedtime=clocklogic.ClockWidget.CurrentTime()
        continue
