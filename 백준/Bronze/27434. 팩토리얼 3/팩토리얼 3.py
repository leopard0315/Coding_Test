# 백준 27434번
# 팩토리얼3

# 입력
N = int(input())
result = 1

# 팩토리얼 계산
if (N == 0):
    print(result)
else:
    for i in range(2,N+1):
        result *= i
    print(result)