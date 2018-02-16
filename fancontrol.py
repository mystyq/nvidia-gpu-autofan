#!/usr/bin/env python
import os
import time

updateInterval = 3
fanSpeed = 45
lastFanSpeed = 20

while True:

    f = os.popen('nvidia-smi -q -d temperature | grep "GPU Current Temp"')
    strToParse = eval(str(f.readlines()))[0]
    currentTemp = int(strToParse[strToParse.index(":")+2:strToParse.index("C\n")-1])

    if currentTemp > 30 and currentTemp < 40:
        fanSpeed = 45
    if currentTemp > 40 and currentTemp < 50:
        fanSpeed = 65
    if currentTemp > 50:
        fanSpeed = 85

    if fanSpeed != lastFanSpeed:
        lastFanSpeed = fanSpeed
        os.system('nvidia-settings -a "[gpu:0]/GPUFanControlState=1" -a "[fan-0]/GPUTargetFanSpeed=' + str(fanSpeed) + '"')

    time.sleep(updateInterval)