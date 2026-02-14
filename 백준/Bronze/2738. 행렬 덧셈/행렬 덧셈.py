# 2738번
# 행렬 덧셈

a = []
b = []

# 입력
N,M = map(int,input().split())

# 첫번째 행렬
for _ in range(N):
    a.append(list(map(int,input().split())))

# 두번째 행렬
for _ in range(N):
    b.append(list(map(int,input().split())))

# 계산후 출력
for i in range(N):
    for j in range(M):
        print(a[i][j] + b[i][j], end= " ")
    print()

# print(a) = print(a,end = "\n")