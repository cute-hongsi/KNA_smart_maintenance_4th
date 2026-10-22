# 입력 (input)
# 주의) 사용자 입력은 항상 "문자열"
# 형식 : 변수 = input("안내문구: ")
# name = input("이름: ")
# age = input("나이: ")
# print(name)

# 형변환 - int(), float(), str()
# print(int(age) + 1)

# print("실습 1")
# birth_year = int(input("태어난 해를 입력하세요: "))
# age = 2026 - birth_year + 1
# print("나이:",int(age),"세")
# height = float("173.5")
# print(height, type(height))

# print("나이:" + str(30))

# country = input("거주 국가를 입력하세요: ")
# city = input("거주 도시를 입력하세요: ")
# print(country,"의" ,city,"에서 거주하시는군요!")

# a = input("정수를 입력하시요: ")
# b = input("또 다른 정수를 입력하시요: ")
# a = int(a)
# b = int(b)
# print(a+b)

# temp = int(input("온도를 입력하시오: "))
# print("30도 이상", temp >= 30)
# print("80도 미만", temp < 80)

a = int(input("A의 점수를 입력하시오:"))
b = int(input("B의 점수를 입력하시오:"))
c = int(input("C의 점수를 입력하시오:"))
print("평균값 :", (a+b+c)/3)
print("A는 B보다 점수가 높다", a > b)
print("A는 C보다 점수가 높다", a > c)
print("B는 C보다 점수가 높다", b > c)