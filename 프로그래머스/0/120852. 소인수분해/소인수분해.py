def solution(n):
    # 소수들을 먼저 찾고
    # 해당 소수들로 나누어준다.
    # 중복되는값은 set안에 넣어줘서 제거하고
    # 리스트로 만들고 오름차순 정렬
    answer = []
    s = set()
    num = 2
    
    while(n != 1):
        for i in range(2,n+1):
            if n % i == 0:
                n = n // i
                s.add(i)
                break
    s = list(s)
    s.sort()
    return s
