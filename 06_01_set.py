# 셋 - 중복 자동 제거, 순서 없음
# 형식: {값1, 값2} 또는 set(리스트)
# - 빈 셋 set()
# logs = ["S01", "S02", "S01", "S03"]
# unique_logs = set(logs)
# print(unique_logs)         # {'S01', 'S03', 'S02'} 셋은 순서가 없어서 인덱싱이 불가 
# print(sorted(unique_logs)) # ['S01', 'S02', 'S03']

# add - 값 추가/ in - 포함 여부 확인
# alerts = {"S01", "S02"}
# alerts.add("S03")
# print(alerts)
# alerts.add("S02")
# print(alerts)
# print("S02" in alerts)

# # 실습4
# logs = ["S01", "S02", "S01", "S03"]
# unique_logs = set(logs)
# print(sorted(unique_logs))
# print(len(unique_logs))

# # 집합 연산 - union(전체) / intersection(공통)/ difference(차이)
# line_a = {"S01", "S02", "S03"}

# 실습 5
# line_a = {"S01", "S02", "S03","S05"}
# line_b = {"S03", "S04", "S05"}
# all_s = line_a.union(line_b)

# common = line_a.intersection(line_b)
# print("공통:",common)
# print("A만:",line_a.difference(line_b))
# print("B만:",line_b.difference(line_a))

# 실습 6
yesterday = {"S01", "S02", "S03",}
today = {"S02","S03", "S05"}
print("신규 이상:",today.difference(yesterday))
print("지속 이상:",today.intersection(yesterday))