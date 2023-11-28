import asyncio

async def main() : 
	token = "텔레 봇 API"
	chat_id = "봇 chat id"

	bot = telegram.Bot(token=token)
	await bot.send_message(chat_id, '보낼 메세지')

asyncio.run(main())