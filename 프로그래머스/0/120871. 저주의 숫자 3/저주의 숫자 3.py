def solution(n):
    a = [] # 3x마을에서 쓰는 숫자 배열 전부 구하기
    num = 1
    for i in range(100):
        while(num % 3 == 0 or '3' in str(num)): # 현재 3이 들어간 숫자를 잡지 못하고 있음
            num += 1
        a.append(num)
        num += 1
    
    print(a)
    return a[n-1]