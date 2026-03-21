# 백준 4716번
# 풍선
import sys
input = sys.stdin.readline

while(1):
    N,A,B = map(int,input().strip().split())
    # 종료조건
    if N == 0 and A == 0 and B == 0:
        break

    distance = 0
    C = []
    for i in range(N):
        k,a,b = map(int,input().strip().split())
        c = abs(a-b)
        d = [k,a,b,c]
        C.append(d)

    # 정렬
    C.sort(key=lambda x: (-x[3]))

    # C = [k,a,b,c]
    for i in range(N):
        # a >= b
        # b 사용
        if C[i][1] >= C[i][2]:
            if B - C[i][0] >= 0:
                distance += C[i][2] * C[i][0]
                B -= C[i][0]
            else: # b일부만 사용
                distance += C[i][2] * B + C[i][1] * (C[i][0]-B)
                A = A - (C[i][0] - B)
                B = 0
        # a < b
        # a사용
        else:  # a전부 사용
            if A - C[i][0] >= 0:
                distance += C[i][1] * C[i][0]
                A -= C[i][0]
            else: # a 일부만 사용
                distance += C[i][1] * A + C[i][2] * (C[i][0]-A)
                B = B - (C[i][0]-A)
                A = 0
    # 출력
    print(distance)