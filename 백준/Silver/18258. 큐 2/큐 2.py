# 백준 18258번
# 큐2

import sys
from collections import deque
input = sys.stdin.readline

q = deque()

N = int(input())
for _ in range(N):
    n = list(map(str,input().split()))
    # 명령 1 : push X -> q.append(x)
    if n[0] == "push":
        q.append(int(n[1]))
    # 명령 2 : pop -> q.popleft() 왼쪽 / q.popright() 오른쪽꺼 빼기
    elif n[0] == "pop":
        print(q.popleft() if q else -1)
    # 명령 3 : size -> q.qsize()
    elif n[0] == "size":
        print(len(q))
    # 명령 4 : empty -> len(q)
    elif n[0] == "empty":
        print(0 if q else 1)
    # 명령 5 : front -> q[0]
    elif n[0] == "front":
        print(q[0] if q else -1)
    # 명령 6 : back -> q[-1]
    elif n[0] == "back":
        print(q[-1] if q else -1)

    # if len(q) != 0 :
    # == if q: