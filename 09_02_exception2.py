# try-except-else-finally
# -else : 예외가 하나도 안 났을 때만 실행
# -finally : 성공/실패 상관없이 무조건 마지막 실행

# text = "62.5"
# try:
#     temp = float(text)
# except ValueError:
#     print("변환 실패")
# else:
#     print("변환 성공",temp)
# finally:
#     print("종료")

# 실습 1
# try:
#     f = open("data/09_ict_inspection.csv", "r", encoding="utf-8")
#     first = f.readline()
#     print(first.strip())
# except FileNotFoundError:
#     print("파일이 존재하지 않습니다")
# finally:
#     f.close()
# print("파일을 닫았습니다.")

'''
# 실습 2
try:
    with open("data/09_ict_inspection_dirty.csv", encoding="utf-8") as f:
        rows = f.readlines()[1:]        # 슬라이싱(헤더 빼려고)
except FileNotFoundError:
    rows = []

total = 0.0
skipped = 0
for line in rows:
    try:
        total += float(line.split(",")[2])      # 측정값(2열)
    except(ValueError,IndexError):
        skipped += 1
        continue

print("합계:", round(total,1), "/건너뜀", skipped)
'''

'''
# 실습 2
try:
    with open("data/09_ict_inspection_dirty.csv", "r", encoding="utf-8") as f:
        rows = f.readlines()[1:]   # 헤더 제외
except FileNotFoundError:
    rows = []

total = 0.0
valid = 0
for line in rows:
    try:
        value = float(line.split(",")[2])
        total += value
        valid += 1
    except (ValueError, IndexError):
        pass
    # 실습 2번 pass 사용 / 실습 3번 skippes+= 1 , continue 사용
print("합계:", round(total,1),"/유효:",valid,"/제외:",len(rows)-valid)
'''

# 실습 5
def check_value(text,lo=0.0, hi=5000.0):
    v = float(text)

    # TODO : 범위 밖이면 ValueError발생
    if not (lo <= v <= hi):
        raise ValueError(f"정상 범위 밖: {v}")
    return v

for t in ["128.5", "결측", "999"]:
    try:
        print("통과:", check_value(t))
    except ValueError as e:
        print("제외:", e)