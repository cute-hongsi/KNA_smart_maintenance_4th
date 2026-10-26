# 실습 1
# n = int(input("끝 숫자 N을 입력하세요: "))
# for i in range(1, n+1):
#     print(i)
# for i in range(2, n+1, 2):
#     print(i)
# for i in range(n,0, -1):
#     print(i)

# 실습 2
# n = int(input("숫자 N을 입력하세요: "))
# total = 0
# for i in range(1, n+1):
#     total += i
# print("합:",total)

# 실습 3
# for dan in range(2,10):
#     for su in range(1,10):
#         print(dan,"x",su,"=",dan*su)
#     print("---")

# 실습 4
n = int(input("측정 횟수를 입력하시오: "))
count = 0
for i in range(n):
    value = int(input("측정값을 입력하세요: "))

    if value >= 80:
        count += 1
print("초과개수:5",count)