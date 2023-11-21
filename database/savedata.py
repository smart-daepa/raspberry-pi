#실행방법: savedata.py measurement_name column1 value1 column2 value2 ...
#실행예시: savedata.py testtable col1 11 col2 22 col3 33
#실행결과: testtable에 { 'col1': 11, 'col2': 22, 'col3': 33 } 데이터 저장.
#주의사항: value는 float으로 형변환하기 때문에 숫자만 입력 가능.

#!/usr/bin/python3

import sys
from datetime import datetime
from influxdb import InfluxDBClient as influxdb

now = datetime.now()
date = now.year + now.month + now.day + ' ' + now.hour + now.minute
measure = sys.argv[1]
col_names = []
col_values = []
fields_values = {}

argc = len(sys.argv)
if argc%2 == 1:
    print("columns과 value의 짝이 맞지 않습니다.")

for i in range(2, argc, 2):
    col_index = 0
    col_names.append(sys.argv[i])
    col_values.append(sys.argv[i+1])

for i in range(0, len(col_names)):
    fields_values[col_names[i]] = float(col_values[i])

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

