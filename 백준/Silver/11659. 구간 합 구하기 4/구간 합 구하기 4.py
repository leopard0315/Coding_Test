# 11659번
# 구간 합 구하기4
import sys

input = sys.stdin.readline

# 입력
N , M = map(int,input().split())
A = list(map(int,input().split()))

presum = [0] * (N+1)

for i in range(N):
    presum[i+1] = presum[i] + A[i]

for _ in range(M):
    n,m = map(int,input().split())
    print(presum[m] - presum[n-1])