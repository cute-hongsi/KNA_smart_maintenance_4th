# replace - 바꾸기/지우기
# 형식 : 문자열.replce('바꿀것','새것')
# - 모두 바꾸기, 결과 저장 필요

# print("정 상 가 동".replace(' ',''))
# print('010-1234-5678'.replace('-',''))
# 체이닝 활용 가능 -> 여러 종류 문자 대체 차례대로 변경

# split - 구분자로 나누기(결과->리스트)
# 형식 : 문자열.split('구분자') (구분자 생략 = 공백 기준)
# print('A1 A2 A3'.split())

# text = '설비 정상 가동'
# print(text.replace('정상','점검'))

# text = 'PUMP A 03'
# print(text.split())

text = 'a,b,c,d'
# print(text.split(','))
print(text.split(',',1))