----
# 라즈베리 파이 카메라 사용 & 텔레그램 연동 - 이강현
## 라즈베리파이에 카메라를 연결한 후 카메라 작동확인 코드 입력
>raspistill -o 파일명.jpg

## 카메라 작동 확인 후 다음 코드를 실행
~$ vim test_camera.py
~~~
import time
from picamera2 import Picamera2, Preview

picam = Picamera2()

config = picam.create_preview_configuration()
picam.configure(config)

picam.start_preview(Preview.QTGL)

picam.start()
time.sleep(2)
picam.capture_file("test-python.jpg")

picam.close()
~~~

## 텔레그램 봇 생성
> 1. 텔레그램에서 봇생성 봇 검색 - botfather
> 2. botfather내에 채팅창에 다음을 입력
> /start -> /newbot -> 봇이름_bot -> 사용자 봇 token 확인
> 3. 텔레그램 사용자 검색으로 Get My Id 검색후 입장
> /start로 봇 user ID, chat ID 확인
> 4. 봇 생성 완료

## 라즈베리파이에 Telegram API 설치
> 1. pip3 install python-telegram-bot --upgrade
> 2. git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive

## 텔레그램 봇 확인 용 코드 실행
~$ vim telebot_test.py
~~~
import asyncio

async def main() : 
	token = "텔레 봇 API"
	chat_id = "봇 chat id"

	bot = telegram.Bot(token=token)
	await bot.send_message(chat_id, '보낼 메세지')

asyncio.run(main())
~~~

## 카메라와 텔레그램 연동 코드
timerbot.py를 수정하여 daepa_cam.py작성

## timerbot에서 수정할 내용
> 1. 카메라가 지정한 시간마다 찍도록 스케줄링해야한다.
> 2. 텔레그램에서 /start 로 실행시켜야한다.
> 3. 텔레그램에서 /stop 으로 정지시켜야한다.
> 4. 불필요한 명령어는 삭제한다.

## daepa_cam.py의 기능
> 1. 라즈베리파이에 연결된 파이 카메라를 사용하여 사진촬영
> 2. 촬영된 사진을 텔레그램 봇에 전송
> 3. 텔레그램 명령어인 /start 실행시 정해둔 시간마다 사진촬영하여 텔레그램에 전송
> 4. 정지 기준이 정해지지않았으므로 무한반복됨
----
