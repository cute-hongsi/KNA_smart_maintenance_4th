import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# isnan - 결측값 위치 찾기
# - 결측값 : 값이 빈 칸 -> 0이 아니라 값을 모름

x = np.array([2.0, np.nan, 4.0])
print(x)

# nanmean, nanstd - 결측값을 무시한 통계
temp = np.array(70.1, np.nan, 71.2, 70.8)
print(np.mean(temp))
print(round(np.nanmean(temp),2))

#nanmean, nanmax, nanmin

# 백분위수, 산분위수 - percentile, quantile
# - 데이터를 크기순으로 줄 세웠을 때 특정 위치의 값
# - 25, 50, 75 백분위수 -> 1사분위, 중앙값, 3사분위

vib_s = np.array([2.0, 2.2, 2.5, 2.8, 3.0, 6.5])
print(round(float(np.percentile(vib_s, 25)),2))
print(round(float(np.percentile(vib_s, 75)),2))

# 여러 자리 한번에
print(round(np.percentile(vib_s, [25, 50, 75]),2))

# quantile : 25 -> 0.25
print(np.round(float(np.quantile(vib_s, 0.25)),2))

# 사분위 기반 이상치 범위 - IQR

q1, q3 = np.percentile(vib_s, [25,75])
iqr = q3- q1
upper = q3 + 1.5 * iqr
print(vib_s[vib_s > upper])