import time
from picamera2 import Picamera2,Preview

#실행한 폴더에 image.jpg 사진 촬영
def take():
    camera = Picamera2()
    camera.start_preview(Preview.QTGL)

    preview_config = camera.create_preview_configuration(main={"size":(800,600)})
    camera.configure(preview_config)
    camera.start()
    time.sleep(2)
    camera.capture_file("image.jpg")
    camera.close()
