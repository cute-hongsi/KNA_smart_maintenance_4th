# 메서드 - 점(.) 문법
# 형식 : 문자열.메서드이름() -> 꼭 괄호를 붙여야 실행
# word = 'python'
# upper() : 모두 대문자/ lower() : 모두 소문자
# capitalize() : 문장 첫 글자만 대문자/ title() : 단어마다 첫 글자 대문자
# print(word.upper)       #PYTHON
# print(word.count('p'))  #1
# print(word)             #python(원본값 그대로)

# print('NORMAL'.lower())

# word = 'upper'
# print(word.upper())

# word = 'WARNING'
# print(word.lower())

# word = 'kim chul soo'
# print(word.title())

# word_1 = 'Fault'
# word_2 = 'FAULT'
# print(word_1 == word_2)
# print(word_1.lower() == word_2.lower())

# 확인 매서드 : is*** 메서드는 참/거짓 반환
# print('ABC'.isupper(),'abc'.islower())

# 공백 정리 - strip
# 형식: .strip() = 앞뒤 공백 제거
# raw = '  정상  '
# print('['+raw+']')          #[  정상  ]
# print('['+raw.strip()+']')  #[정상]

# .lstrip() -> 왼쪽 공백 제거/ .rstrip() -> 오른쪽 공백 제거
# 주의) strip은 '앞뒤' 공백만 제거, 가운데 공백 제거 x
# strip() 으로 특정 문자 제거 -> strip('문자')

# s = "###정상###"
# print(s.strip('#'))

# print('ABC'.isupper(),'ABC'.islower())
# print('abc'.isupper(),'abc'.islower())
# print('Abc'.isupper(),'Abc'.islower())

# word = 'Sensor_LOG.CSV'
# print(word.lower().startswith('sensor'))
# print(word.lower().endswith(".csv"))

# s = '  가동중  '
# print('['+s.strip()+']')

# s = ' 대기 '
# print(s.lstrip()+'/'+s.rstrip())

# s = '***경고***'
# print(s.strip('*'))

# print('WARNING'.strip().lower())

text = ' 경보 '
print('['+text+']')
text = text.strip()
print('['+text+']')