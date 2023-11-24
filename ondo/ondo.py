import serial

def start():

	port = '/dev/ttyACM0'
	brate = 9600
	cmd = 'temp'

	seri = serial.Serial(port, baudrate = brate, timeout = None)

	seri.write(cmd.encode())

	while True:
		if seri.in_waiting != 0:
			line = seri.readline().decode()
			temp, humi= map(float, line.split())
			
			return(temp, humi)
