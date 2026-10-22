# tel = '0101234568789'
# print(len(tel))

# in/ not in ; 포함/ 불포함 여부 (결과 bool)
# 형식 : '찾을 것' in 문자열
# message = '설비 고장 발생'
# print('고장' in message)
# print('정상' in message)

#count
# 형식 : 문자열.count('x') -> 개수
# word = 'sensor-01-temp'
# print(word.count('-'))

#find
# 형식 : 문자열.find('x') - > 처음 나오는 위치
# word = 'temp_2024'
# print(word.find("_"))
# print(word.find('-'))

#index
# 주의) 위치를 반환하지만, 없으면 오류
# email = 'hong@company.com'
# at = email.index('@')
# print(at)
# print(email[:at])       #hong

#startswitch/ endswitch
# 형식 : 문자열.startswith('x') -> bool

# name = 'sensor_log.csv'
# print(name.startswith('sensor'))
# print(name.endswith('.csv'))

label_1 = 'WARNING'
label_2 = 'warning'
print(label_1==label_2)