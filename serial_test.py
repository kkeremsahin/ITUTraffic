#
#     YOUR IMPORTS HERE
#
#

import serial as sr

ARDUINO_OK = 10
RASPBERRY_OK = 11

READ_SIGN = 19

ser = sr.Serial('/dev/ttyUSB0',9600)
	
while int.from_bytes(ser.read(1), byteorder = 'little') != ARDUINO_OK :
	print("Arduino is NOT ready!")

ser.write(b'r')

ser.reset_input_buffer()
ser.reset_output_buffer()

print("Initialized !")

while 1:
	
	# check if the READ_SIGN signal is here
	if( int.from_bytes(ser.read(1), byteorder = 'little') == READ_SIGN ):
		
		#read_sign()
		
	
	
