# while - 조건이 참인 동안 반복
# 형식:
# while 조건식:           (조건이 거짓이 되는 순간 멈춤)
# for - '몇 번'이 정해졌을 때, while은 '언제 끝날지 모르지만 조건으로 멈출 때' 사용

# count = 1
# while count <= 3:
#     print(count)
#     count += 1
# 주의) 무한루프를 막으려면 (1)언제가 거짓이 될 조건, (2)반복문 안에서 그 조건을 갱신시켜줄 수 있는 코드가 필요
# 처음부터 조건이 거짓이면 한 번도 실행되지 않는다.

answer = 7
num = 0
while num != answer:
    num = int(input("정답을 입력하시오:"))
print("정답입니다!")