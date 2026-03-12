# 백준 10816번
# 숫자 카드2

import sys
from collections import Counter
input = sys.stdin.readline

# 입력
N = int(input())
a = list(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))

c = []
count = Counter(a)

# dict을 활용하여 단어의 개수 세기
for i in range(M):
    c.append(count.get(b[i],0))

# 출력
print(*c)