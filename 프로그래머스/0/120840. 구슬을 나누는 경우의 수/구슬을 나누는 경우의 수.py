def solution(balls, share):
    answer = 1
    dif = balls - share # 차이값
    # share 가 dif보다 큰경우
    if share >= dif:
        for i in range(balls,share,-1):
            answer *= i
        for j in range(1,dif+1):
            answer = answer // j
    
    # dif가 share보다 큰 경우
    else:
        for i in range(balls,dif,-1):
            answer *= i
        for j in range(1,share+1):
            answer = answer // j
    
    return answer