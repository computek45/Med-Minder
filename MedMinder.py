# Med Minder created by Kevin Wright this is a smaller version Med Tracker.
# This program was made to me to remember to take my medications.
# I also thought it other people do the same.
# Here looking at you kid, LOL. Hope you stay in good health!!!
# Completed on Janurary 23, 2019.

# I use alarm.py for the check the time when the medication needs to be
# taken and to make the buzzer sound.

# alarm.py
# Raspberry Pi Alarm Clock
# 2014, Ismail Uddin
# www.scienceexposure.com

# ~/raspberrypi/buzzer.py
# Script forked from Simon Monk's 'Pi Starter Kit' repo
# https://github.com/simonmonk/pi_starter_kit

import time
import RPi.GPIO as GPIO
from buzzer import buzz
import os

# I connected the piezo buzzer to GPIO pin 23.

# morning time variables
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

# midday time variables
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0

# afternoon time variables
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0

# evening time variables
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0

# With inputing the time use the 24 hour format excluding leading zeros.
# midnight would be just 0.

medtime1 = 800 # Mornig time
medtime2 = 1200 # Mid-day time
medtime3 = 1600 # Afternoon time
medtime4 = 2000 # Evening time

# Replace Med Name 1-6 the the names of the medications you need to take.
# You can make the list bigger or smaller to suite your needs.

medname = ['Med Name 1', 'Med Name 2', 'Med Name 3', 'Med Name 4', 'Med Name 5', 'Med Name 6' ]

# the true and false words below should correspond with the medication above,
# of when you need to take them.

morningtime = [True, True, True, True, True, True] # corresponding with medtime1 listed above.
middaytime = [True, True, False, False, False, False] # corresponding with medtime2 listed above.
afternoontime = [False, False, True, True, False, False] # corresponding with medtime3 listed above.
eveningtime = [False, False, False, False ,True, True] # corresponding with medtime4 listed above.

a = len(morningtime)
g = len(middaytime)
m = len(afternoontime)
s = len(eveningtime)

for b in range(a):
    if morningtime[b] == True:
        c += 1
    else:
        e += 1
        
    if c != 0:
        time1 = True
    else:
        time1 = False

for h in range(g):
    if middaytime[h] == True:
        i += 1
    else:
        k += 1

    if i != 0:
        time2 = True
    else:
        time2 = False

for n in range(m):
    if afternoontime[n] == True:
        o += 1
    else:
        q += 1

    if o != 0:
        time3 = True
    else:
        time3 = False

for t in range(s):
    if eveningtime[t] == True:
        u += 1
    else:
        w += 1

    if u != 0:
        time4 = True
    else:
        time4 = False

def setmedtime():
    if currenttime < medtime1:
        alarmtime = medtime1
    if currenttime > medtime1 and currenttime < medtime2:
        alarmtime = medtime2
    if currenttime > medtime2 and currenttime < medtime3:
        alarmtime = medtime3
    if currenttime > medtime3 and currenttime < medtime4:
        alarmtime = medtime4
        
def maintitle():
    os.system('clear')
    print('Running Med Minder')
    
def takenomeds():
    buzz(1500,0.5)
    print('')
    print('There are no medications scheduled to taken at this time.')
    time.sleep(61)
    maintitle()

def takemorningmeds():
    f = 0
    if time1 == False:
        # takenomeds()
        # if you want to be reminded that no medications to taken at this
        # time, then uncomment the command above.
        pass
    else:
        buzz(900,0.5)
        time.sleep(0.5)
        print('')
        print('Time to take the following medication(s)')
        for d in range(a):
            if morningtime[d] == True:
                f += 1
                print(medname[d])
                if a == e + f:
                    time.sleep(61) 
                    maintitle()
                    
def takemiddaymeds():
    l = 0
    if time2 == False:
        # takenomeds()
        # if you want to be reminded that no medications to taken at this
        # time, then uncomment the command above.
        pass
    else:
        buzz(900,0.5)
        time.sleep(0.5)
        print('')
        print('Time to take the following medication')
        for j in range(g):
            if middaytime[j] == True:
                l += 1
                print(medname[j])
                if g == k + l:
                    time.sleep(61) 
                    maintitle()
                                                                                         
def takeafternoonmeds():
    r = 0
    if time3 == False:
        # takenomeds()
        # if you want to be reminded that no medications to taken at this
        # time, then uncomment the command above.
        pass
    else:
        buzz(900,0.5)
        time.sleep(0.5)
        print('')
        print('Time to take the following medication')
        for p in range(m):
            if afternoontime[p] == True:
                r += 1
                print(medname[p])
                if m == q + r:
                    time.sleep(61) 
                    maintitle()
                                                        
def takeeveningmeds():
    x = 0
    if time4 == False:
        # takenomeds()
        # if you want to be reminded that no medications to taken at this
        # time, then uncomment the command above.
        pass
    else:
        buzz(900,0.5)
        time.sleep(0.5)
        print('')
        print('Time to take the following medication')
        for v in range(s):
            if eveningtime[v] == True:
                x += 1
                print(medname[v])
                if s == w + x:
                    time.sleep(61) 
                    maintitle()


maintitle()

try:
    while True:
        currenttime = int(time.strftime("%H%M"))
        
        if currenttime == medtime1:
            takemorningmeds()

        if currenttime == medtime2:
            takemiddaymeds()

        if currenttime == medtime3:
            takeafternoonmeds()

        if currenttime == medtime4:
            takeeveningmeds()

        time.sleep(0.5) # DO NOT REMOVE OR SHORTEN TIME!!!
        # This to keep down the processing power, 0.5 seconds,
        # it keeps the processing power between 1 to 3 percent.
                        
finally:
        GPIO.cleanup()
        print("End")
