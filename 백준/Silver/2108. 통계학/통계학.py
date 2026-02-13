# 백준 2108번
# 그대로 출력하기

import sys
from collections import Counter

input = sys.stdin.readline

A = []
N = int(input())
for _ in range(N):
    A.append(int(input()))

# 1. 산술 평균 / 중앙값/ 최빈값 / 범위
# 정렬 후에 계산
A.sort()
sum1 = round(sum(A) / N)
sum2 = A[(N-1)//2]
sum4 = A[N-1] - A[0]

cnt = Counter(A)

if(N == 1):
    sum3 = A[0]
else:
    cal = cnt.most_common(2) 
    if(cal[0][1] == cal[1][1]):
        sum3 = cal[1][0]
    else:
        sum3 = cal[0][0]

print(sum1)
print(sum2)
print(sum3)
print(sum4)