# Whitecliffe-Timers.py
'''
from datetime import datetime, timedelta

duration = 5
run = input("Enter s to begin...")
period = timedelta(seconds = 1)

nextTime = datetime.now() + period

counter = 0

while run == "s" and counter < duration:
    if nextTime <= datetime.now():
        print("..", counter)
        counter += 1
        # re-evaluate the nextTime variable
        nextTime += period
'''
######### Brocode timer ##########

import time

running = True
seconds = 10
end = 0

while running == True:
    print(seconds)
    time.sleep(1)
    seconds -= 1
    if(seconds <= end):
        running = False
        print(seconds)

print("Happy New Year!")


