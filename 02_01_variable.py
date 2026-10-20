# 변수와 할당 - 값에 이름 붙이기
# 형식 : 변수이름 = 값 <- 오른쪽 값을 왼쪽 이름에 "저장"하라는 명령
temp = 25
name = "센서A"
count = 3

print(temp)
print("temp")
x = 10
x = x + 5
print(x)

# 변수 이름 규칙
# 형식 : 영문자, 숫자, 밑줄 사용 가능/ 숫자로 시작 불가/ 공백 불가
sensor_count = 3    # snake_case
temp2 = 10          # 숫자 사용 가능(숫자로 시작X)
# 2temp = 2         # SyntaxError: invalid decimal literal

# 대소문자 구분, 재할당
temp = 25
Temp = 100
print(temp,Temp)    # 25, 100
# 재할당 : 마지막 저장한 값만 남음
score = 10
score = 20
score = 30
print(score)    #30

temp = 25
print(temp)
name = "센서A"
print(name)

temp = 30
print(temp)
temperature = temp
print(temperature)

my_number = 5
print(my_number)
mood = "happy"
print(mood)

age = 27
label = "나이"
print(label, age)

print("실습 5")
x = 10
print(x)    #10
x = x + 5
print(x)    # 15
x = x * 2 
print(x)    # 30

print("실습 6")
a = 100
b = a
a = 999
print(a)
print(b)

print("실습 7")
temp = 25
print(temp)
score = 90
print(score)    #NameError: name 'Score' is not defined.

print("실습 8")
temp = 25 #온도(섭씨)
count = 3 #센서 개수
#temp = 100
print(temp)

print("실습 9")
x = 5
x = 10
x = x + 1
print(x)    # 11

print("실습 10")
name = "센서A"
temp = 25
print("설비")
print(name, temp)

print("실습 11")
a, b = 25, 3
device_temp = a
sensor_count = b
print(device_temp)

print("실습 12")
x,y,z = 1,2,3
width, height = 4,3
print(width), print(height)