# 백준 28278번
# 스택2

import sys
input = sys.stdin.readline

# 입력
N = int(input())
a = []

for _ in range(N):
    n = list(map(int,input().split()))
    # 명령1
    if (len(n) == 2):
        a.append(n[1])
    else:
        order = int(n[0])
        # 명령2
        if (order == 2):
            if (len(a) != 0) :
                res = a.pop()
                print(res)
            else:
                print(-1)
        # 명령3
        elif (order == 3):
            print(len(a))
        # 명령4
        elif (order == 4):
            if len(a) == 0 :
                print(1)
            else:
                print(0)
        # 명령5
        elif (order == 5):
            if len(a) != 0:
                print(a[-1])
            else:
                print(-1)