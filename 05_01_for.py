# range(시작,, 끝, 증가값)
# for i in range(1,10,2):
    # print(i)

# for i in range(5, 0, -1):
#     print(i)

#누적 변수 패턴(합계, 갯수, 평균)
total = 0
for i in range(1,6):
    total += i
print("합계:", total)

count = 0
for i in range(1,11):
    if i > 5:
        count += 1
print("개수:", count)

total = 0
count = 0
for i in range(1,6):
    total += i; count += 1 
if count > 0:
    print("평균:", total/count)