import serial, sys

sys.path.append('../database')
from function_savedata import savedata

port = '/dev/ttyACM0'
brate = 9600
	
def soil():
	seri = serial.Serial(port, baudrate = brate, timeout = None)

	while True:
		if seri.in_waiting != 0:
			line = seri.readline().decode()
			soil_humi = float(lin.split(":")[-1].strip())
			
			savedata("soil", "soil_humi", soil_humi)
			
