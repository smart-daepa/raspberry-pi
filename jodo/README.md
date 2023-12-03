## 조도센서로 LED제어를 제어하여 조도센서 값을 DB 저장 - (김수지)

## 조건
1. 조도센서 값 500을 기준으로 led 제어(어두울때: 빨간불, 밝을 때: 파란불, 조금 밝을때: 노란불)
2. 식물 생장 LED을 3색 신호등 모듈로 대체하는것이므로 빨간불: 식물 생장 LED 'ON' 으로 가정
3. 1시간 단위로 조도센서 값을 DB에 저장

## 결과
(연결후 모습)

![image](https://github.com/smart-daepa/raspberry-pi/assets/113170868/0656a4d1-f1d0-4943-a510-ca4596655c17)

(DB에 저장된 모습)
![image](https://github.com/smart-daepa/raspberry-pi/assets/113170868/ace179d8-9ad2-458a-b195-800dbb3c32d5)

(DB에 최종적으로 저장된 모습)
![image](https://github.com/smart-daepa/raspberry-pi/assets/113170868/ca007fc2-84f5-42cf-a267-2bb1697f2548)


## 진행사항
1. 1시간 단위로 저장되는것을 확인함
2. 6시간이 지나면 LED가 더 이상 켜지지 않는지 확인해봐야함
3. DB에 값이 들어갔으나 이상하게 들어간 부분이 있어 수정해야함(수정완료)

## 보완사항
1. 6시간이 지나도 LED가 여전히 켜지는 점
