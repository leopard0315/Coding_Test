# 백준 2446번
# 별 찍기 - 9

# 입력
N = int(input())

# 절반 출력1
for i in range(0,N):
    star = " " * i + "*" * (2*(N-i)-1)
    print(star)

# 절반 출력2
for j in range(2,N+1):
    star = " " *  (N- j) + "*" * (2*j - 1)
    print(star)