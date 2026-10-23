# name = '홍길동'
# age = 25
# print(f'{name}님은 {age}살입니다')

# code = 'PUMP_A'
# temp = 97
# print(f'설비 {code}, 온도 {temp}도')

# a = 90
# b = 85
# c = 87
# print(f'평균 {(a+b+c)/3}')

# value = 87.456
# print(f'{value:.1f}')
# print(f'{value:.2f}')

text = '5,sensor_2,WARNING,0.78912'
p = text.split(',')
print(f'[센서{p[1]}]상태{p[2].lower()},측정값{float(p[3]):.2f}')