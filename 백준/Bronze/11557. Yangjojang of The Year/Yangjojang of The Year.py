T = int(input())
for i in range(T):
    N = int(input())
    A = []
    B = []
    for j in range(N):
        a,b = input().split()
        A.append(a)
        B.append(int(b))
    for k in range(N):
        if(B[k] == max(B)):
            print(A[k])