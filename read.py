# Write your code here :-)
from __future__ import print_function
import Adafruit_DHT as dht
from time import sleep

#sleepTime = 2 #sensor rate 0.5 Hz, so sleepTime should be greater than 2
sensor = dht.DHT22
pin = 4 #GPIO 4

def c2f(c):
    return (c * 9 / 5) + 32 #returns temperature in F for a given temperature in C

def read(verbose=False):
    #sleep(sleepTime)
    h,t = dht.read_retry(sensor,pin)
    if verbose:
        print('Temp: {:.02f}*F'.format(c2f(t)),' Humidity: {:.01f}%'.format(h))
    return [c2f(t),h]
