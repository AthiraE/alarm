import os
import datetime
from playsound import playsound
os.system('cls')

alarmH = int(input("What hour would you like to set an alarm"))
alarmM = int(input("What minute would you like to set an alarm"))

amPm = str(input("am or pm"))
os.system('cls')
print("waiting for alarm",alarmH,alarmM,amPm)
if (amPm=="pm"):
    alarmH=alarmH + 12
    while(1==1):
        if (alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute ):
            print("Time to woke up!!")
            playsound('G83U6ER-alien-alarm.wav')
            break

