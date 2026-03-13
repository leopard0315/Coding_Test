# 백준 1946번
# 신입 사원

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    a = []
    for i in range(N):
        b = list(map(int,input().split()))
        a.append(b)

    a.sort(key=lambda x : x[1])
    a_value2 = a[0][0]

    cnt = 1 
    for i in range(1,N):
        if a[i][0] == 1:
            cnt += 1
            break
        if a[i][0] < a_value2:
            a_value2 = a[i][0]
            cnt += 1
        else:
            continue
    print(cnt)