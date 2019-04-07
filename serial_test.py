#
#     YOUR IMPORTS HERE
#
#


import serial as sr

ARDUINO_OK = 10
RASPBERRY_OK = 11

READ_SIGN = 19


###  FUNCTION DEFINITIONS


def read_sign():
	
	#read your sign here 
	
	
	outputData = A1   ##write a type from  '### OUTPUT TYPES'
	
	ser.write(outputData)
	
	return outputData

### OUTPUT TYPES

LEFT = b'L'
RIGHT = b'R'
FORWARD = b'F'
A1 = b'1'
A2 = b'2'
A3 = b'3'
B1 = b'4'
B2 = b'5'
B3 = b'6'

### Initialize 


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
		
		print(" Reading sign...")
		
		out = read_sign().decode("utf-8")
		
		print("Serial Sent:" +  out)
		
	


