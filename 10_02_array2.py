import numpy as np

# 인덱싱, 슬라이싱
# a = np.array([0,1,2,3,4])
# print(a[0], a[-1])
# print(a[1:4])
# print(a[::2])

# 실습 1
# rpm = np.array([4603, 4720, 4650, 4800, 4550,
#                    4700, 4900, 4620, 4750, 4603])
# print(rpm[0])
# print(rpm[-1])
# print(rpm[1:4])
# print(rpm[0:10:2])

# 실습 2
data = np.array([[4603,2],[58,5],
                 [1216,1],[4967,21]])
print(data[2])
print(data[:,0])
print(data[:,1])