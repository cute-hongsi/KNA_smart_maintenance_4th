# 리스트
# 형식: 이름 = [값1, 값2, ...]
# - 리스트는 여러 값을 '순서대로' 한 이름에 담는다.

# temps = [25, 26, 24 ,28 ,27]    #숫자 리스트
# mechines = ["펌프", "모터", "압축기"]
# mixed = ["펌프", 87, True]      #종류가 달라도 한 리스트에 담을 수 있다

# print(len(temps))       #5
# print(len([]))          #0

# temps = [25, 26, 24 ,28 ,27]
# print(temps)
# print(len(temps))
# empty = []
# print(empty)
# print(len(empty))

# temps = [25, 26, 24 ,28 ,27, 23]
# print(temps[0],temps[3],temps[-1])

# uph = [100, 111, 120, 114, 116]
# first = uph[0]
# last = uph[-1]
# print(first+last)
# print((first+last)/2)

# temps = [22, 23, 24, 25, 26, 27 ,28, 30, 31, 32]
# print(temps[:3])
# print(temps[-3:])
# print(len(temps[:3]))

# first = temps[:6]
# print(first)
# second = temps[-6:]
# print(second)
# print(len(first),len(second))

# 값 바꾸기/ in 존재 확인
# 형식: 리스트[번호] = 새 값/ 값 in 리스트
# nums = [25, 26, 24, 28, 27]
# nums[2] = 99
# print(nums)

# 값 추가 - append, insert, extend
# 형식 : 리스트.append(값)/ 리스트.insert(값)/ 리스트.extend(다른 리스트))
# temps = [25,26,240,28,27]
# print(240 in temps)
# i = temps.indes(240)
# temps[i] = 24
# print(temps)
# print(240 in temps)

# temps = []
# temps.append(30)
# print(temps)
# temps.insert(0, 28)
# print(temps)
# temps_2 = [31, 32]
# temps.extend(temps_2)
# print(temps)

# 값 삭제 - remove, pop, del
# 형식 : 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) / del 리스트[위치]

# 정렬, 탐색 - sort, reverse/ count, index
# 형식: 리스트.sort()   .reverse()  .count(값)  .index(값)

# l = [25,26,24,28,26,999]
# l.remove(999)
# print(l)
# print(l.pop(1))
# del l[0] 
# print(l)

# temps = [22, 24, 24, 26, 27, 28, 30]
# temps.sort()
# print(temps)
# temps.reverse()
# print(temps)
# print(temps.count(24))
# print(temps.index(24))