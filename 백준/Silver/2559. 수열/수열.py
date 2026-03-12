# 백준 2559번
# 수열
# 시간 초과가 안나려면 이중 for문을 없애야한다.
import sys
input = sys.stdin.readline

# 입력
N, K = map(int,input().split())
a = list(map(int,input().split()))
b = []

presum = [0] * (N+1)
 
# 구간합 정의
for i in range(N):
    presum[i+1] = presum[i] + a[i]

for j in range(N-K+1):
    b.append(presum[j+K] - presum[j])

# 출력
print(max(b))