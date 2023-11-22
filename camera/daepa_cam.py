import logging
from picamera2 import Picamera2, Preview
import time
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import schedule
import sys

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

#텔레봇 chat id 입력
chat_id = "chat id"

#실행한 폴더에 image.jpg 사진 촬영
def takePhoto():
    camera = Picamera2()
    camera.start_preview(Preview.QTGL)

    preview_config = camera.create_preview_configuration(main={"size":(800,600)})
    camera.configure(preview_config)
    camera.start()
    time.sleep(2)
    camera.capture_file("image.jpg")
    camera.close()

#텔레그램에서 /start 입력시 사진촬영 후 텔레그램 전송 반복
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    await update.message.reply_text("대파 감시를 시작합니다")
    while True:
        await alarm(update, context)
        #10초마다 반복
        time.sleep(10)

#start에서 실행되어 찍은 사진을 텔레그램에 전송
async def alarm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the alarm message."""
    takePhoto()
    time.sleep(1)
    job = context.job
    await context.bot.sendPhoto(chat_id, photo=open("image.jpg","rb"))
    context.bot.send_message(chat_id, text='boop')

#텔레그램 명령어
def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    #텔레봇 token입력
    application = Application.builder().token("token").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("alarm", alarm))
    application.add_handler(CommandHandler("stop", stop))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
