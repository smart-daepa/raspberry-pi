#사전준비: influxdb에 'project'라는 이름으로 데이터베이스를 만들어야함. (create database project)
#함수호출예시: savedata('measurement 이름', 'column1', 'value1', 'column2', 'value2', ... )
#정상실행시: "Running influxDB OK" 출력
#예외발생시: 상황에 따른 에러메시지 출력

#추가해야하는 라이브러리 
from datetime import datetime
from influxdb import InfluxDBClient as influxdb

#함수 정의
def savedata(measurement_name, *args):
    now = datetime.now()
    date = str(now.year) + str(now.month) + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute)
    measure = measurement_name
    col_names = []
    col_values = []
    fields_values = {}
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
    return
