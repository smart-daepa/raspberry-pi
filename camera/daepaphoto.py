import logging
import time
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from takePhoto import takePhoto

import sys

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

#텔레봇 chat id 입력
chat_id = "chat_id"

#takephoto로 찍은 사진을 텔레그램에 전송
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    takePhoto()
    time.sleep(1)
    job = context.job
    await context.bot.sendPhoto(chat_id, photo=open("image.jpg","rb"))
    context.bot.send_message(chat_id, text='boop')
    

#텔레그램 명령어
def main() -> None:
    #텔레봇 token입력
    application = Application.builder().token("token").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("photo", photo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
