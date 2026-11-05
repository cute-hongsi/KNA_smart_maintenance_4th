import numpy as np

F = 'data/11_diecasting_series.csv'

# ct = np.genfromtxt(F, delimiter=",",skip_header=1, usecols=1)
# print(ct.shape, ct.dtype)

def colc(c):
    return np.genfromtxt(F,delimiter=",",skip_header=1, usecols=c)

# 자리 찾기
# fancy indexing : 여러 위치에 한번에 추출 가능 (떨어진 자리도 한번에 가능)
vib = np.array([2.1, 2.3, 2/0, 5.8])
pick = np.array([0,3])
print(vib[pick])

# 정렬과 정렬 순서
# - sort, argsort : 원래 자리 번호 돌려줌

print(np.sort(vib))
print(np.argsort(vib))