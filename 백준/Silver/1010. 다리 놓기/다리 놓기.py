T = int(input())
for l in range(T):
    N, M = map(int,input().split()) # N <= M
    a ,b,c = 1,1,1
    for i in range(1,M+1):
        a = a * i
    for j in range(1,N+1):
        b = b * j
    for k in range(1,M-N+1):
        c = c * k
    a = a // (b * c)
    print(a)