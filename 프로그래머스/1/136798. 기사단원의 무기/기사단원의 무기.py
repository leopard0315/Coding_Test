# 기사 1 ~number
import math

def solution(number, limit, power):
    # 약수 먼저 찾기
    measure = []
    
    # 시간 초과가 났던 부분
    # 
    for i in range(1,number+1):
        count = 0
        for j in range(1,math.isqrt(i)+1):
            if i % j == 0:
                # 마지막 부분 제곱근인 경우에만 1번 더하고
                # 아니라면 둘이 제곱근을 기준으로 짝지어있기때문에, 2번씩을 더한다.
                if j * j == i:
                    count += 1
                else:
                    count += 2
                    
        measure.append(count if count <= limit else power)
    
    return sum(measure)