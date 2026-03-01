# 백준 2441번
# 별 찍기 - 4

N = int(input())
for i in range(N):
    star = " " * (i) + "*" * (N-i)
    print(star)