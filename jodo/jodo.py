import serial, sys

sys.path.append('../database')
from function_savedata import savedata

port = '/dev/ttyACM0'
brate = 9600

def jodo():
	seri = serial.Serial(port, baudrate = brate, timeout = None)

	while True:
		if seri.in_waiting != 0:
			line = seri.readline().decode()
			jodo = float(lin.split(":")[-1].strip())
			
			savedata("jodo", "jodo", jodo)
