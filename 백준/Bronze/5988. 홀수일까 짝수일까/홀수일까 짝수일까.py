# 백준 5988번
# 홀수일까 짝수일까

N = int(input())
for _ in range(N):
    k = int(input())
    if(k%2 == 0):
        print("even")
    else:
        print("odd")