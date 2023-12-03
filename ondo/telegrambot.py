import telegram, sys, asyncio
from datetime import datetime
from util import secret


async def sendTelegramMessage(jodo, temp, humi):
	
	content = ''
	formatted_now = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
	
	if temp > 25:
		content = '\n현재 온도가 대파를 키우기엔 높습니다. \n적정 온도(5도~25도)를 맞춰주세요.'
	elif temp < 5:
		content = '\n현재 온도가 대파를 키우기엔 낮습니다. \n적정 온도(5도~25도)를 맞춰주세요.'
	else:
		content = '\n대파가 무럭무럭 성장하고 있습니다.'
		
	text = '안녕하세요\n'
	text += '현재 시간: ' + formatted_now
	text += '\n현재 온도: ' + str(temp)
	text += '\n현재 습도: ' + str(humi) + '\n'
	text += '\n현재 조도: ' + str(jodo) + '\n'
	text += content
	
	token = secret.getToken()
	chat_id = secret.getId()
	bot = telegram.Bot(token=token)
	
	await bot.sendMessage(chat_id, text)
