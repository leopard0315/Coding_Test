# 백준 27890번
# 특별한 작은 분수

# 입력
x,N = map(int,input().split())

# 분수의 높이 계산
for i in range(0,N):
    # 짝수인 경우
    if (x % 2 == 0):
        x = int(x // 2) ^ 6
    # 홀수인 경우
    else :
        x = (2 * x) ^ 6
        
# 출력
print(x)