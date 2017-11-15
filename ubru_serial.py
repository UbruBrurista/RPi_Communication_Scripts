#!/usr/bin/env python

import serial

ser = serial.Serial(
 port='/dev/ttyACM0',
 baudrate = 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)

print("connected to: " + ser.portstr)
count=1

while True:
    for line in ser.read():

        print(line)
        count = count+1

ser.close()