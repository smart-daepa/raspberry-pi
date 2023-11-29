import serial
import time
from influxdb import InfluxDBClient

# InfluxDB 설정
influx_client = InfluxDBClient(host='localhost', port=8086, database='project')

# 시리얼 통신 설정
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# LED 동작 시간 제한 설정(광합성은 6시간이면 충분함으로)
max_led_on_time = 6 * 60 * 60
current_led_on_time = 0

# InfluxDB에 저장(1시간단위로 저장)
influxdb_save_interval = 60 * 60
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
        json_body = [
            {
                "measurement": "brightness",
                "tags": {"bright": "bright"},
                "fields": {"value": value}
            }
        ]

        # 1시간이 지난 경우에만 InflowsDB에 데이터 저장
        if time.time() - last_influxdb_save_time >= influxdb_save_interval:
            influx_client.write_points(json_body)
            last_influxdb_save_time = time.time()
    except ValueError as e:
        print(f"Error converting to int: {e}")
        print(f"Data causing the error: {response}")

    # 1초 대기
    time.sleep(1)

    # 6시간이 지나면 빨간 LED가 계속 켜져 있지 않도록
    current_led_on_time += 1
    if current_led_on_time >= max_led_on_time:
        ser.write(b'0')  # 밝을 때 명령 전송
        current_led_on_time = 0
