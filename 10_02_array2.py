import numpy as np

# 인덱싱, 슬라이싱
# a = np.array([0,1,2,3,4])
# print(a[0], a[-1])
# print(a[1:4])
# print(a[::2])

# 배열 연산
a = np.array([1,2,3])
b = np.array([10,20,30])
print(a+b)
# 같은 위치 값끼리 계산(반복문 필요x)
# 사칙 연산 모두 같은 방식으로 계산

# 스칼라 연산
# - 숫자 하나를 배열 전체에 적용, 크기를 맞출 필요가 없다
# - 연산 숫자는 수학과 같아 곱하기 먼저
print(a*10+3)

# 브로드캐스팅
table = np.array([[72,2.4],[95,6.8]])
print(table.shape)
base = np.array([70,2.0])
print(table-base)


# 파일에서 배열로 불러오기(np.loadtxt)
rpm = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",     # 값을 나누는 기호
                 skiprows = 1,      # 첫 줄(제목)은 건너뜀
                 usecols = 4)       # 5번째 열 = 회전수
print(rpm)