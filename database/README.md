# influxdb에 센서값 저장하기

#### column이름과 value를 입력받아 저장하는 savedata.py 코드 설명

##### 사용하는 라이브러리
```python3
from datetime import datetime
from influxdb import InfluxDBClient as influxdb
```

##### 함수 선언부 (범용적으로 사용하기 위해 가변인자 사용)
```python3
def savedata(measurement_name, *args):
```

##### 데이터베이스에 현재 시간 저장
```python3
now = datetime.now()
date = str(now.year) + str(now.month) + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute)
```

##### column이름과 value를 각각의 리스트에 저장
```python3
flag = 0
for v in args:
    if flag == 0:
        col_names.append(v)
        flag = 1
    else:
        col_values.append(v)
        flag = 0

   if flag == 1:
        print("column과 value의 짝이 맞지 않습니다.")
        return
```

##### influxdb에 저장을 위한 딕셔너리 생성
```python3
for i in range(0, len(col_names)):
    fields_values[col_names[i]] = float(col_values[i])
```

##### influxdb에 저장
```python3
data = [{
    'measurement' : measure,
    'tags' : {
        'date' : date
    },
    'fields' : fields_values
}]

client = None
try:
    client = influxdb('localhost', 8086, 'root', 'root', 'project')  # database명: project
except Exception as e:
    print("Exception" + str(e))
if client is not None:
    try:
        client.write_points(data)
    except Exception as e:
        print("Exception write " + str(e))
    finally:
        client.close()
print("Running influxDB OK")
return
```

##### 실행예시와 결과
###### 호출하는 코드
```python3
temp = 20.3
humi = 30.4

savedata('ondo1', 'temp', temp, 'humi', humi)
```
###### influxdb에 저장된 모습
![savedata_py 저장성공사진_자른거](https://github.com/smart-daepa/raspberry-pi/assets/113410132/4c7402af-85ac-4231-9a58-32bc16e197e5)


# 실제 사용 모습

### 아두이노에서 시리얼 통신을 이용하여 라즈베리파이로 전송하는 메시지의 예시
jodo 331 ondo 26.08 15 soil_moisture 27 

### seri.py에서 savedata.py를 호출하는 코드
```python3
# jodo
avedata(arr[0], "sensorValue", float(arr[1]))
# ondo
savedata(arr[2], "temp", float(arr[3]), "humi", float(arr[4]))
asyncio.run(telegrambot.sendTelegramMessage(arr[1], float(arr[3]), float(arr[4])))
# soil
savedata(arr[5], "humi", float(arr[6]))
```

### 정상적으로 저장된 모습
##### 온도
![select_ondo](https://github.com/smart-daepa/raspberry-pi/assets/113410132/c7bbbd7d-f09d-4915-a327-4b26157e22be)
##### 조도
![select_jodo](https://github.com/smart-daepa/raspberry-pi/assets/113410132/c37ef3f0-b86a-4575-907e-bbb0346dbffa)
##### 토양수분
![select_soil](https://github.com/smart-daepa/raspberry-pi/assets/113410132/4948254d-3e78-43e5-9279-3beb49c20791)


