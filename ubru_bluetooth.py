#!/usr/bin/env python
import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *

GPIO.setmode(GPIO.BOARD) 	# board pin numbering
GPIO.setup(11, GPIO.OUT) 	# GPIO 0 == pin 11
GPIO.setup(13, GPIO.OUT) 	# GPIO 2 == pin 13

# Initialize 
GPIO.output(11, True)		# Set Pin 11 to 0V
GPIO.output(13, True)		# Set Pin 13 to 0V


# Open Bluetooth connection on rfcomm0
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e492929" 	# Identical to UUID in Android Application

advertise_service( server_sock, "UbruPiServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )


while True:          
	print "Waiting for connection on RFCOMM channel %d" % port

	client_sock, client_info = server_sock.accept()
	print "Accepted connection from ", client_info
	try:
		# Read data from Android app
		data = client_sock.recv(1024)
	    #if len(data) == 0: break
		print "received [%s]" % data
		# Button 1 was pressed
		if data == 'test1':
			data = 'Test 1: Pin 11!'
			data = '1'
			GPIO.output(11, True)
			GPIO.output(13, False)
		# Button 2 was pressed
		elif data == 'test2':
			data = 'Test 2: Pin 13!'
			data = '2'
			GPIO.output(11, False)
			GPIO.output(13, True)
		# Failed data transfer
		else:
			data = 'Fail!'
			GPIO.output(11, False)
			GPIO.output(13, False)

		# Send data from Arduino back to Android app
		client_sock.send(data)
		print "sending [%s]" % data


	except IOError:
		pass

	except KeyboardInterrupt:

		print "disconnected"

		client_sock.close()
		server_sock.close()
		ser.close()
		print "all done"

		break