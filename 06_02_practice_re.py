# 실습 1
# sensors = {"모터온도":78,"진동":0.5}
# print(sensors["모터온도"])
# sensors['펌프압력'] = 95
# sensors['진동'] = 1
# print(sensors)
# print(sensors.get("모토온도",0))
# print("모터온도" in sensors)

# 실습 2
# sensors = {"모터온도":78,"진동":0.5}
# d = {'펌프압력':95}
# sensors.update(d)
# print(sensors)
# del sensors["진동"]
# print(len(sensors))

# 실습 3
# sensors = {"모터온도":78,"진동":0.5}
# avg = sum(sensors.values())/len(sensors.keys())
# print("평균:",round(avg,2))

# top = ""
# high = 0
# for name, value in sensors.items():
#     if value > high:
#         high = value
#         top = name
# print("최댓값 센서:",top, high)

# 실습 4
# names = ['온도', '진동', '압력']
# values = [78, 0.5, 95]
# sensors = dict(zip(names,values))
# print(sensors)

# for name, value in sensors.items():
#     print(name, value)

# 실습 5
# measure = {"온도":78, "진동":0.5, "압력":84}
# limits = {'온도':70, '진동':1, '압력':90}

# warning = []        # 임계값을 초과한 센서 이름들을 모아서 출력
# for name, value in measure.items():     # measure은 딕셔너리니까, items를 쓸 수 있음
#     if value > limits[name]:            # 키 값으로 limits의 값을 부를 수 있음
#         warning.append(name)
# print(warning)

# 실습 6
# plant = {
#     "1번모터": {"온도":78,"상태":"정상"},
#     "2번펌프": {"압력":95,"상태":"경고"}
# }

# print(plant["1번모터"]['온도'])

# for name, info in plant.items():
#     if '경고' == info['상태']:
#         print(name,"점검 필요")

# 실습 7
