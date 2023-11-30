import serial
import time
from influxdb import InfluxDBClient
from datetime import datetime

# InfluxDB 설정
influx_client = InfluxDBClient(host='localhost', port=8086, database='project')

# 시리얼 통신 설정
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# LED 동작 시간 제한 설정(광합성은 6시간이면 충분함으로)
max_led_on_time = 6 * 60 * 60
current_led_on_time = 0

# InfluxDB에 1시간단위로 저장
influxdb_save_interval=60*60
last_influxdb_save_time = time.time()

while True:
    # 어두울 때 명령 전송
    ser.write(b'1')

    # 아두이노로부터 조도 값 수신
    response = ser.readline().decode('latin-1').strip()
    print(f"Received: {response}")  # 수신한 데이터 출력

    try:
        # 수신한 데이터에서 숫자 부분 추출하여 InfluxDB에 저장
        value = int(''.join(char for char in response if char.isdigit() or char in ['-', '.']))
        
        # Get the current time in seconds since the epoch
        current_time = int(time.time() * 1e9)  # Convert to nanoseconds

        # Convert current time to datetime object
        dt_object = datetime.fromtimestamp(current_time / 1e9)  # Convert back to seconds for datetime
        
        json_body = [
            {
                "measurement": "brightness",
              
                "time": current_time,  # Specify the timestamp in nanoseconds
                "fields": {
                    "jodo": value,
                                     
                    "current_time": dt_object.strftime("%Y-%m-%d %H:%M:%S")  # Format current time as YYYY-MM-DD HH:MM:SS
                }
            }
        ]

        # 1시간이 지난 경우에만 InfluxDB에 데이터 저장
        if current_time - last_influxdb_save_time >= influxdb_save_interval * 1e9:
            influx_client.write_points(json_body)
            last_influxdb_save_time = current_time

            # Increment current_led_on_time
            current_led_on_time += influxdb_save_interval
            print(f"Current LED On Time: {current_led_on_time}")

            # Check if 6 hours have passed
            if current_led_on_time >= max_led_on_time:
                ser.write(b'0')  # 밝을 때 명령 전송
                print("Turning off the red LED")
                current_led_on_time = 0  # Reset the counter
                print("Resetting LED On Time Counter")
    except ValueError as e:
        print(f"Error converting to int: {e}")
        print(f"Data causing the error: {response}")
