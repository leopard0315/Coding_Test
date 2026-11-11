def solution(num, total):
    # num이 홀수인 경우와 짝수인 경우를 나누어서 구한다.
    a = []
    # num이 홀수인 경우
    if num % 2 != 0:
        # 중간값
        num1 = total // num
        # 중간값 기준 왼쪽
        for i in range(num1-1,num1 - (num-1)//2-1,-1):
            a.append(i)
        # 중간값 기준 오른쪽
        for j in range(num1,num1 + (num-1)//2+1 ):
            a.append(j)
            
    # num이 짝수인 경우
    else:
        # 중간값
        num1 = total // num # 3
        # 중간값 기준 왼쪽
        for i in range(num1,num1 - num//2, -1):
            a.append(i)
        # 중간값 기준 오른쪽
        for j in range(num1+1,num1+1 + num //2 ):
            a.append(j)
    
    # 오름차순 정렬   
    a.sort()
    # 정답 반환
    return a