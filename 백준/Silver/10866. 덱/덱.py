# 백준 10866번
# 덱

import sys
input = sys.stdin.readline
from collections import deque
d = deque()

N = int(input())
for _ in range(N):
    order = list(map(str,input().split()))
    # 명령 8가지
    if order[0] == "push_front":
        d.appendleft(int(order[1]))
    elif order[0] == "push_back":
        d.append(int(order[1]))
    elif order[0] == "pop_front":
        print(d.popleft()) if d else print(-1)
    elif order[0] == "pop_back":
        print(d.pop()) if d else print(-1)
    elif order[0] == "size":
        print(len(d))
    elif order[0] == "empty":
        print(0) if d else print(1)
    elif order[0] == "front":
        print(d[0]) if d else print(-1)
    elif order[0] == "back":
        print(d[-1]) if d else print(-1)