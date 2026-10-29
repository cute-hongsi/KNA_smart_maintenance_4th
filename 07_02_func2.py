# 실습 2
# def sensor(name, temp):
#     print(name + str(temp) + " 도")

# sensor("모터", 78)
# sensor("펌프", 92)
# sensor(78, "모터")

# 실습 3
# def sensor(name, temp):
#     print(name + str(temp) + " 도")

# sensor(name="모터", temp=78)
# sensor(temp=92, name="펌프")

# 실습 4
# def calc_avg(a,b):
#     return(a+b)/2

# avg = calc_avg(80,90)
# print(avg)
# print(avg+5)

# 여러 값 반환/언패킹
# - 쉼표로 여러 값을 return하면 튜플로 묶여서 돌아옴 -> 언패킹 가능
# def min_max(values):
#     return min(values), max(values)
# print(min_max([75,10,100]))     #(10, 100)
# low, high = min_max([75,10,100])
# print(low, high)

# none -> return 값이 없는 함수 호출해서 변수로 받을 경우 None

# 실습 5
def sensor_stat(values):
    return min(values), max(values), round(sum(values) / len(values),1)

low, high, avg = sensor_stat([75, 10, 100])

print(low, high, avg)