def solution(n):
    a = [] # 3x마을에서 쓰는 숫자 배열 전부 구하기
    num = 0
    for i in range(n): # 100번 반복해둠
        num += 1
        while(num % 3 == 0 or '3' in str(num)): # 현재 3이 들어간 숫자를 잡지 못하고 있음 -> i에서 num으로 변경
            num += 1
        a.append(num)
        
    # 필요한 부분만 발췌
    return num