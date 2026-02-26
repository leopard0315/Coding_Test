# 백준 25756번
# 방어율 무시 계산하기

# 입력
N = int(input())
A = list(map(int,input().split()))
V = 0

# 증가된 방어율 무시수치 계산
for i in range(N):
    V = 1 - (1-(V/100)) * (1 - (A[i]/100))
    V = V * 100
    
    # 소수 6자리까지 반올림
    print(round(V,6))