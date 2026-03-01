# 백준 2443번
# 별 찍기 - 6

# 입력
N = int(input())

# 출력
for i in range(1,N+1):
    star = " " * (i-1) + "*" * (2 * (N+1 - i)-1)
    print(star)
