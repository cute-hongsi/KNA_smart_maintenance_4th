# try-except 구조
# try:
#     temp = int("스물")
# except ValueError:
#     print("ValueError")

# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("ZeroDivisionError")

# try:
#     print(underfined_var)
# except NameError:
#     print("NaverError")

# 실습2
# try:
#     temp = int(input("온도를 입력하세요: "))
#     print("입력한 온도:", temp)
# except ValueError:
#     print("숫자를 입력하세요.")
# print("프로그램이 계속됩니다.")

# # 여러 except
# row = "P-01,102".split(",")
# try:
#     code_no = int(row[3])
# except ValueError:
#     print("숫자 아님")
# except IndexError:
#     print("칸 부족")

# 실습 3
try:
    value = int(input("측정값: "))
    result = 100 / value
    print("결과: ", result)
except ValueError:
    print("숫자가 아님")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
print("프로그램 계속")