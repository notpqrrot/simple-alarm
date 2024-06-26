# Simple timer by notpqrrot/lapis

# If you dont have pygame installed, simply use os.system command, which is why os has already been imported
#Inside the parantheses for pygame.mixer.Sound, simply add the path to the sound that you want to play!
import os
import time
import datetime

import pygame
date_format = '%H:%M:%S'
def countdown(total_seconds):

    while total_seconds>0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end = "\r")
        time.sleep(1)
        total_seconds-=1
        if total_seconds == 0:

            print("The timer is at zero!")
            pygame.init()
            pygame.mixer.init()
            sound = pygame.mixer.Sound('/Users/medhabhutanni/Desktop/Python/sounds/wsg.mp3')
            sound.set_volume(0.75)
            sound.play()

            responsed = input("Snooze?: ")
            if responsed == 'no':

                print("Thanks for using the alarm!")
            else:
                pygame.mixer.stop()
                mins = int(input("How many more minutes?: "))
                total_seconds = total_seconds + (mins*60)



current = datetime.datetime.now()
current1 = current.strftime('%H:%M:%S')
now = datetime.datetime.strptime(current1,'%H:%M:%S')
t0 = time.time()
later = input("Enter when timer ends: ")
t1 = time.time()
typing = t1-t0
typing = round(typing)
end = datetime.datetime.strptime(later,'%H:%M:%S')
am_pm = input("AM or PM?: ")
if am_pm == 'AM' and end<now:
    end+=datetime.timedelta(days=1)
if am_pm == 'PM' and end<now:
    end+=datetime.timedelta(hours=12)

difference = end - now

total_seconds = difference.total_seconds()
total_seconds = total_seconds - typing
print("Timer has started!")
print("Time remaining...")
countdown(total_seconds)

