import telegram, sys, asyncio
sys.path.append('/home/admin/201844079/raspberry-pi/util')
from datetime import datetime
import secret

async def sendTelegramMessage():
	token = secret.getToken()
	chat_id = secret.getId()
	bot = telegram.Bot(token=token)
	text = '안녕하세요' + str(datetime.now())
	await bot.sendMessage(chat_id, text)

asyncio.run(sendTelegramMessage())
