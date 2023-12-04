import serial, sys, asyncio

sys.path.append('./database')
from function_savedata import savedata
from ondo import telegrambot
from jodo import jodo
from soil import soil

port = '/dev/ttyACM0'
brate = 9600
	
def main():
	seri = serial.Serial(port, baudrate = brate, timeout = None)
	cnt = 0
	while True:
		if seri.in_waiting != 0:
			line = seri.readline().decode()
			if cnt > 0:
				print(line)
				arr = list(map(str, line.split()))
				# jodo
				savedata(arr[0], "sensorValue", float(arr[1]))
				# ondo
				savedata(arr[2], "temp", float(arr[3]), "humi", float(arr[4]))
				try:
					asyncio.run(telegrambot.sendTelegramMessage(arr[1], float(arr[3]), float(arr[4])))
				except telegram.error:
					print("텔레그램 오류 발생. 재실행 시도...")
					asyncio.run(telegrambot.sendTelegramMessage(arr[1], float(arr[3]), float(arr[4])))
				# soil
				savedata(arr[5], "humi", float(arr[6]))
				
			cnt+=1
			print(cnt)

main()
