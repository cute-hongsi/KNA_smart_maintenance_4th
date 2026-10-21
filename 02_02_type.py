# 자료형

count = 3       #int 정수
temp = 25.5     #flot 실수
name = "센서A"  #str 문자열

ok = True       # bool 불린형 - 참/거짓
no = False      # 앞을 대문자로 표기할 것

# type() -> 자료형을 알려줌
print(type(25))     #<class 'int'>
print(type(name))   #<class 'str'>
print(type(ok))     #<class 'bool'>

#자료형마다 다른 동작
print(3+5)      # 8 (숫자 더하기 = 계산)
print("3"+"5")  # 35 (문자 더하기 = 이어 붙이기)

print("실습 1")
count = 3
temp = 27.5
name = "센서A"
is_ok = True
print(count, temp, name, is_ok)

print("실습 2")
print(type(count))
print(type(temp))
print(type(name))
print(type(is_ok))

print("실습 3")
print(type(100))    #int
print(type(100.0))  #float 
print(type("100"))  #str

print("실습 4")
print(3+5)
print("3"+"5")
print("good"+"morning")

print("실습 5")
print(3 > 2)
print(5 == 5)

print("실습 6")
count = 100
print(type(count))
count = 100.0
print(type(count))
count = "hello"
print(type(count))

print("실습 7")
device_temp = 30
check_count = 5
device_name = "센서B"
is_nomal = True