# 백준 10845번
# 큐
import sys
from collections import deque
q = deque()
input = sys.stdin.readline

# 입력
N = int(input())
for i in range(N):
    order = list(map(str,input().split()))

    # 6가지 명령어 처리
    if order[0] == "push":
        q.append(int(order[1]))
    elif order[0] == "pop":
        print(q.popleft()) if q else print(-1)
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        print(0) if q else print(1)
    elif order[0] == "front":
        print(q[0]) if q else print(-1)
    elif order[0] == "back":
        print(q[-1]) if q else print(-1)