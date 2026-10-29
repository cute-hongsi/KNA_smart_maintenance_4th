# 함수 설계와 활용

# 기본값 인자 : 인자 생략 시 기본값 사용
# 형식:
# def 함수(매개변수, 선택=기본값):

# 거의 항상 같은 값을 매번 적는 번거로움을 줄임, 필요할 때만 덮어쓴다
# def report(name, value, unit="도"):
#     print(f'{name}:{value}{unit}')

# report("압축기1", 75.3)     #압축기1:75.3도
# report("펌프1", 7.2, "bar") #펌프1:7.2bar

# 실습 1
# def report(value, limit=80):
#     if value > limit:
#         print(value, "→ 경고")
#     else:
#         print(value,"→ 정상")

# report(78)
# report(95)
# report(50,30)

# 지역변수와 범위(스코프)
# - 함수 안의 변수, 함수 바깥 변수를 읽을 수 있지만, 바깥에서는 한수 안 지역변수를 읽을 수 X
# def calc():
#     result = 10+5 #지역변수
#     return result #밖에서 사용하려면 return으로 내보내야함

# print(calc())

# x= 10
# def change():
#     x = 20      #함수 내부의 지역변수

# change()
# print(x)        #10(함수 바깥의 x값 변경 X)

# 실습 2
# def calc():             # 함수 선언
#     result = 10 + 5     # 지역변수 생성
#     return result

# print(calc())
# print(result)           # 함수 밖에서 해당 지역변수 호출 -> NameError

# 함수 조합(함수 설계: 입력/처리/출력)
# def get_avg(values):
#     return sum(values) / len(values)

# def judge(avg, limit=80):
#     if avg > limit:
#         return "위험"
#     else:
#         return "정상"

# temps = [75, 88, 91]
# avg = get_avg(temps)
# print(round(avg,1), judge(avg))

# 실습 3
# def minus(before, after):
#     return after - before

# def judge(change):
#     if change > 10:
#         return "위험"
#     else:
#         return "정상"

# temps = [75, 88]
# difference = minus(temps[0],temps[1])
# print(difference, judge(difference))

# 실습 4
def get_avg(values):
     return sum(values) / len(values)

def judge(avg, limit=100):
     if avg > limit:
         return "위험"
     else:
         return "정상"

temps = [75, 85, 100]
avg = get_avg(temps)
print(round(avg,1), judge(avg))