# Write your code here :-)
import RPi.GPIO as gpio
from time import sleep

def toggle(num,states=[0,0,0,0]):
    n = num - 1
    relay_1 = 22
    relay_2 = 27
    relay_3 = 17
    relay_4 = 18
    vals = [relay_1,relay_2,relay_3,relay_4]

    gpio.setmode(gpio.BCM)
    gpio.setup(vals[n],gpio.OUT)
    
    if states[n]:
        gpio.output(vals[n],0)
        states[n] = 0
    else:
        gpio.output(vals[n],1)
        states[n] = 1

    gpio.cleanup()
    return states

states = [0,0,0,0]
for i in range(1,5):
    states = toggle(i,states)
    sleep(1)
for i in range(1,5):
    states = toggle(i,states)
    sleep(1)

    