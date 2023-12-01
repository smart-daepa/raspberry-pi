import serial, sys

sys.path.append('./database')
from function_savedata import savedata
from ondo import telegrambot
from jodo import jodo
from camera import daepaphoto
from soil import soil

port = '/dev/ttyACM0'
brate = 9600
	
def main():
	seri = serial.Serial(port, baudrate = brate, timeout = None)

	while True:
		if seri.in_waiting != 0:
			line = seri.readline().decode()
			arr = list(map(float, line.split()))

			# jodo
			savedata(arr[0], "sensorValue", arr[1])

			# ondo
			savedata(arr[2], "temp", arr[3], "humi", arr[4])
			telegrambot.sendTelegramMessage(arr[1], arr[3], arr[4])

			# soil
			savedata(arr[5], "humi", arr[6])

			# photo
			daepaphoto.photo()
