# 백준 10828번
# 스택
import sys
input = sys.stdin.readline

N = int(input())
a = []

for _ in range(N):
    order = list(map(str,input().split()))
    if order[0] == "push":
        a.append(order[1])
    elif order[0] == "pop":
        print(a.pop()) if a else print(-1)
    elif order[0] == "size":
        print(len(a))
    elif order[0] == "empty":
        print(0) if a else print(1)
    elif order[0] == "top":
        print(a[-1]) if a else print(-1)