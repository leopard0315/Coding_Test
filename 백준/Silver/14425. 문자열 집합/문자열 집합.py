# 백준 14425번
# 문자열 집합

# 입력
N,M = map(int,input().split())
S = []
cnt = 0

# 집합 S에 포함되어있는 문자열 추가
for _ in range(N):
    S.append(str(input()))

for i in range(M):
    s = str(input())
    if (s in S):
        cnt += 1
    else:
        continue
print(cnt)