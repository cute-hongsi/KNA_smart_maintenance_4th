# 실습 1
# import numpy as np
# temp = np.array([20, 22, 24, 26, 28, 30])
# print(temp)
# fahrenheit = temp * 1.8 + 32
# print(fahrenheit)

# 실습 2
# import numpy as np
# current = np.linspace(0,70,8)
# print(current)

# 실습 3
# import numpy as np
# temp = np.arange(0,40,5)
# print(temp)

# 실습 4
# import numpy as np
# sensor = np.array([[70,18],[72,19],[75,21],[73,20]])
# print("차원",sensor.ndim)
# print("형태",sensor.shape)
# print("개수",sensor.size)

# # 실습 5
# import numpy as np
# current = np.array([18.69, 20.95, 23.42, 25.78])
# print(current.dtype)
# current_int = current.astype(int)
# print(current_int)

# 실습 6
import numpy as np
# sensors = np.array([70,18,72,19,75,21,73,20,70,18,72,19])
# new_sensors = sensors.reshape(3,4)
# print(new_sensors)

# 실습 7
flat = np.array([30, 15.44, 4603, 30, 18.69, 4603,
                30, 62.48, 4967, 30, 18.37, 4603])
table = flat.reshape(4,3)
print(table)
print(table.flatten())