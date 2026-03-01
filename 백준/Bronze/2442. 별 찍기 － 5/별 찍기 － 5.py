# 백준 2442번
# 별 찍기 - 5

# 입력
N = int(input())

# 출력
for i in range(1,N+1):
    star = " " * (N-i) + "*" * (2*i-1)
    print(star)