# 백준 30236번
# 증가 수열

# 입력
t = int(input())

# t번 반복
for _ in range(t):
    # 정수 n 입력
    n = int(input())
    # 배열 생성
    a = list(map(int,input().split()))
    b = [0] * len(a)
    c = 1
    
    if(a[0] == 1):
        c += 1    
    b[0] = c
    for i in range(1,len(a)):
        if(a[i] == (c + 1)):
            c += 2
        else :
            c += 1
        b[i] = c
    print(b[-1])