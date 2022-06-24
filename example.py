#!/bin/env python
from CO2Meter import *
from datetime import datetime
import time

file = open("/dev/hidraw0", "a+b", 0)
Meter = CO2Meter(file)
while True:
    measurement = Meter.get_data()
    measurement.update({'timestamp': datetime.now()})
    print(measurement)
    time.sleep(5)
