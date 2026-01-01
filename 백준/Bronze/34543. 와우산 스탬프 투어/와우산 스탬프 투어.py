# W = 걸음수
# P = 방문 장소
# point = 점수
N = int(input())
W = int(input())
point = 0

# 기본점수
point = N * 10
# 추가점수1
if(N >= 3):
    point = point + 20
    # 추가점수2
    if(N == 5):
        point += 50
if(W > 1000):
    point = point - 15
    if(point < 0):
        point = 0
print(point)