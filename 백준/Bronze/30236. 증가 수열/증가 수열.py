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
    c = 0

    # 배열 비교
    for i in range(0,len(a)):
        # 해당 배열 값과 +1 증가한 값이 동일할때 +2 증가 
        # 아니면 그대로 +1 증가
        if(a[i] == (c + 1)):
            c += 2
        else :
            c += 1
        b[i] = c
        
    # 최솟값 출력
    print(b[-1])