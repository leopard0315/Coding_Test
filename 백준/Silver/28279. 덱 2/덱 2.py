# 백준 28279번
# 덱2

import sys
input = sys.stdin.readline
from collections import deque
d = deque()

N = int(input())
for _ in range(N):
    order = list(map(int,input().split()))
    # 명령 8가지
    if order[0] == 1:
        d.appendleft(order[1])
    elif order[0] == 2:
        d.append(order[1])
    elif order[0] == 3:
        print(d.popleft()) if d else print(-1)
    elif order[0] == 4:
        print(d.pop()) if d else print(-1)
    elif order[0] == 5:
        print(len(d))
    elif order[0] == 6:
        print(0) if d else print(1)
    elif order[0] == 7:
        print(d[0]) if d else print(-1)
    elif order[0] == 8:
        print(d[-1]) if d else print(-1)