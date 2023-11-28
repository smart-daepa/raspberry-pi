import serial, sys

sys.path.append('../database')
from function_savedata import savedata

port = '/dev/ttyACM0'
brate = 9600
	
def ondo():
	seri = serial.Serial(port, baudrate = brate, timeout = None)

	while True:
		if seri.in_waiting != 0:
			line = seri.readline().decode()
			temp, humi= map(float, line.split())
			
			savedata("ondo", "temp", temp, "humi", humi)
			
			return temp, humi
