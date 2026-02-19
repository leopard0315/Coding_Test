# 백준 1977번
# 완전제곱수

# 입력 (0 < M <= N <= 10000)
M = int(input())
N = int(input())

# 최소값, 합산값
min = N+1
sum = 0

# 완전제곱수가 M~N사이인지 확인하기
for i in range(1,101):
    num = i ** 2
    if (M <= num and num <= N):
        if (num < min):
            min = num
        sum += num
    else:
        continue

# 출력시 완전제곱수가 없을때와 있을때
if (min == N+1 or sum == 0):
    print(-1)
else :
    print(sum)
    print(min)