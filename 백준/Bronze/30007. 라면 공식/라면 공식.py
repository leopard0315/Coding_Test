# 백준 30007번
# 라면 공식

N = int(input())
for _ in range(N):
    A,B,X = map(int,input().split())
    W = A * (X - 1) + B
    print(W)