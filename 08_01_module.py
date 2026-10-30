# 모듈/ 패키지/ 라이브러리
# - 모듈 : 기능을 모아둔 .py 파일 하나
# - 패키지 : 모듈을 모아둔 폴더
# - 라이브러리 : 위에 사항들을 통칭

# import 방식
# 형식 : import 모듈/ from 모듈 import 기능/ import 모듈명 as 별칭
# import math             # math라는 모듈을 통째로 불러옴
# print(math.sqrt(16))    # 4.0
# from math import sqrt, ceil # 일부만 불러옴 -> 모둘명 없이 바로 사용
# print(sqrt(16), ceil(4.2))
# import math as m
# print(m.sqrt(16))

# print(random.randint(1,100))
# print(datetime.datetime.now())

# 실습2
# import random
# import math
# value=random.randint(1,100)
# print(math.sqrt(value))

# ///////
# 경로와 os 모듈
# - 파일을 다루려면 어디에 있는지 경로를 알아야 한다
# 1) 절대경로
#   - 최상위부터 전체 주소
# 2) 상대경로
#   - 지금 실행중인 위치를 기준으로 한 주소

# import os
# print("현재 실행 위치(절대경로):", os.getcwd())

# # 폴더 유무 확인
# print(os.path.exists("data"))

# # 폴더 목록 확인
# files = os.listdir("data")
# print(files)

# 실습 3
# import os
# print(os.getcwd())
# files = os.listdir("data")
# for file in files:
#     if file.endswith(".csv"):
#         print(file)

# 폴더명 + 파일명 -> 경로
# import os
# path = os.path.join("data", "08_press_13_261029_3.csv")

# if os.path.exists(path):
#     print("파일 경로:", path)

# 실습 4
# import os
# path = os.path.join("data", "08_press_13_261029_3.csv")
# print(os.path.exists(path))

# if os.path.exists(path):
#     print("파일 있음")
# else:
#     print("파일 없음")

# # 실습 5
# import os
# import datetime

# path = "data"
# file = os.listdir(path)
# count = len(file)

# now = datetime.datetime.now()

# print(f"파일 {count}개, 점검 시각 {now}")


# 실습 6
import os
path = "data"
file = os.listdir(path)
csv = []
for f in file:
    if f.endswith(".csv"):
        path = os.path.join(path,f)
        csv.append(path)
print("[CSV]목록",csv)