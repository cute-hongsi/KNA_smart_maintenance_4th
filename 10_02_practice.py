import numpy as np
# 실습 1
# rpm = np.array([4603, 4720, 4650, 4800, 4550,
#                    4700, 4900, 4620, 4750, 4603])
# print(rpm[0])
# print(rpm[-1])
# print(rpm[1:4])
# print(rpm[0:10:2])

# 실습 2
# data = np.array([[4603,2],[58,5],
#                  [1216,1],[4967,21]])
# print(data[2])
# print(data[:,0])
# print(data[:,1])

# 실습 3
# base = np.array([30, 40, 50, 60, 30,
#                 30, 40, 50, 60, 30])
# m = base.min()
# M = base.max()
# print("min",m,"max",M)
# print(np.round((base-m)/(M-m), 2))

# 실습 4
# rpm = np.array([4603, 4603, 58, 4603, 4603,
#                 1216, 4603, 4603, 1217, 4603])
# #전류 데이터(실습용 예시값)
# current = np.array([2,2,21,2,3,
#                     2,2,3,2,147])
# data = np.array([[4603,2],[4603,21]])
# low_rpm = rpm < 2000
# # 회전수 2000 미만
# print(rpm[low_rpm])
# # 회전수 2000 미만 또는 전류 25 초과
# print(rpm[rpm < 2000], current[current > 25])
# # 개수
# print(np.sum(low_rpm))
# print(np.sum((rpm < 2000) | (current <25)))
# # 비율
# print(np.mean(low_rpm) * 100, "%" )
# # - low_rpm : True False 배열 -> True: 1, False: 0
# print(np.mean((rpm < 2000) | (current <25))*100,"%")

# 실습 5
# 파일에서 배열로 불러오기(np.loadtxt)

# 실습 6
# sensor = np.array([[4600, 30], [4700, 35], [4500, 28], [4800, 40]])
# print(sensor.mean(axis=0))
# print(sensor.std(axis=0))

# 실습 7
# rpm = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",
#                  skiprows=1,
#                  usecols=4)

# print(round(rpm.mean(),1))
# print(round(rpm.std(),1))
# print(rpm.min(), rpm.max())

# 실습 8
# tq = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",
#                  skiprows=1,
#                  usecols=4)
# high = tq[tq>10]
# print(np.round(high,1))
# print(high.size, round(high.mean(), 1))

# 실습 9
rpm_tq = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",
                 skiprows=1,
                 usecols=(4,5))
rpm = data[:,0]
print(rpm_tq.shape, rpm_tq.dtype)
low = rpm[rpm < 2000]
print(low.size, round(low.mean(),1))
print(round(rpm.mean(),1))