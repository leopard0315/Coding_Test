# 백준 2444번
# 별 찍기 - 7

# 입력
N = int(input())

# 절반 출력1
for i in range(1,N+1):
    star = " " * (N - i) + "*" * (2 * i - 1)
    print(star)

# 절반 출력2
for j in range(1,N):
    star = " " * (j) + "*" * (2 * (N-j)-1)
    print(star)