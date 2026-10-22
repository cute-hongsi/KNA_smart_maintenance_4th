# 인덱싱 - 위치 번호로 글자 하나 꺼내기
# 형식 : 문자열[번호]   (첫 글자 = 0번)

# word = 'PYTHON'
# print(word[0], word[2], word[5])        # P T N
# # 음수 인덱스 : 뒤에서부터 -1, -2, ...
# print(word[-1], word[-2])               # N O

# word = 'SIGNAL'
# print(word[0],word[2],word[5])
# print(word[-1],word[-2])

# 슬라이싱 - 구간으로 잘라내기
# 형식 : 문자열[시작:끝] (시작은 포함하고 끝은 제외)
# print(word[1:4])
# 생략 가능
# - 시작 생략 = 처음부터
# - 끝 생략 = 끝까지
# - 둘다 생략 = 전체
# print(word[:3])     # PYT
# print(word[3:])     # HON
# print(word[:])      # PYTHON

# word = 'SIGNAL'
# print(word[-3:])
# print(word[3:])

# word = 'temp_sensor'
# print(word[-6:])

# word = 'sensor_01'
# print(word[-2:])

# step 간격 주기
# 형식 : 문자열 [시작:끝:간격]
# print(word[::2])
# print(word[1::3])

word = 'SIGNAL'
# print(word[::2])
print(word[::-1])