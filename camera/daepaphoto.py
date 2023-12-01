import logging
import time
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import secret

from picamera2 import Picamera2,Preview

import sys

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

#텔레봇 chat id 입력
chat_id = secret.getId()
token = secret.getToken()

def take():
    camera = Picamera2()
    camera.start_preview(Preview.QTGL)

    preview_config = camera.create_preview_configuration(main={"size":(800,600)})
    camera.configure(preview_config)
    camera.start()
    time.sleep(2)
    camera.capture_file("image.jpg")
    camera.close()


#takephoto로 찍은 사진을 텔레그램에 전송
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    take()
    time.sleep(1)
    job = context.job
    await context.bot.sendPhoto(chat_id, photo=open("image.jpg","rb"))
    context.bot.send_message(chat_id, text='boop')
    

#텔레그램 명령어
def main() -> None:
    #텔레봇 token입력
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("photo", photo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
