# 백준 2445번
# 별 찍기 - 8

# 입력
N = int(input())

# 절반 출력1
for i in range(1,N+1):
    star = "*" * i + " " * (2* (N- i)) + "*" * i
    print(star)

# 절반 출력2
for j in range(N-1,0,-1):
    star = "*" * j + " " * (2* (N- j)) + "*" * j
    print(star)