import asyncio

async def main() : 
	token = "�ڷ� �� API"
	chat_id = "�� chat id"

	bot = telegram.Bot(token=token)
	await bot.send_message(chat_id, '���� �޼���')

asyncio.run(main())