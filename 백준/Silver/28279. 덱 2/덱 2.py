from collections import deque

import sys
input = sys.stdin.readline
N =int(input())
d = deque()
for _ in range(N):
    order = list(map(int,input().split()))
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