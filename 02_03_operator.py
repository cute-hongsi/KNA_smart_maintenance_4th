# 연산자
# - 산술, 비교, 논리 연산자

# 산술 연산자
# 형싱 : +, -, *, /,//(몫),%(나머지), **(거듭제곱)

# 우선순위
# - 곱셈, 나눗셈 등이 우선, 괄호를 이용하여 변경 가능

# 복합 할당
# 형식 : score += 10 <-> score = score + 10

# 문자열 연산
# +, * 가능 주의)자료형이 같은 것끼리 연산할 수 있다

print(" 실습 1")
a = 17
b = 5
print(a+b, a-b, a*b, a/b)
print(a//b)
print(a%b)
print(a**b)

print("실습 2")
a = 1
b = 2
c = 3
print((a+b+c)/3)
print(a**2)
print(a*b*c)

# 비교 연산자
# ==같다 != 다르다 < > >= <=

print("실습 3")
print(5 == 5)
print(5 != 7)
print(7 > 5)
print(7 < 5)
print(7 >= 5)
print(7 <= 5)

print("실습 4")
temp = 85
press = 5
print(60<= temp <= 90)
print(3 <= press <= 5)
print(60 <= temp <= 90 and 3 <= press <= 5)

print("실습 5")
count = 100
print(count)
count += 50
print(count)
count -= 30
print(count)
count += 5
print(count)

print("실습 6")
print(23/500*100,"%")
print((21/24)*100,"%")

print("실습 7")
hour = 500 // 60
min = 500 % 60
print(hour,"시간", min,"분")