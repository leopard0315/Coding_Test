# 23971번 백준
# 입력 & 배열 생성
H,W,N,M = map(int,input().split())
cnt1 = 0
cnt2 = 0

# 가로 카운트 값
for i in range(0,W,M+1):
    cnt1 += 1

# 세로 카운트 값
for j in range(0,H,N+1):
    cnt2 += 1

# 총합 계산
print(cnt1 * cnt2) 