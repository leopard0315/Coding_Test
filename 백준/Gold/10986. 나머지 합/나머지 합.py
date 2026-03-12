# 백준10986번
# 나머지 합
# 입력
import sys
from collections import Counter
input = sys.stdin.readline

N,M = map(int,input().split())
a = list(map(int,input().split()))
b = set()

# 누적합 계산
presum = [0] * (N+1)
for i in range(N):
    presum [i+1] = presum[i] + a[i]

# 누적합의 원소들을 M으로 나눈값을 다시 배열로 생성
# 나머지 개수 세기
reminder = [presum[i] % M for i in range(N+1)]
count = Counter(reminder)

# 같은 나머지끼리 조합해서 계산
cnt = 0
for v in count.values():
    cnt += v * (v-1) // 2

# 출력
print(cnt)