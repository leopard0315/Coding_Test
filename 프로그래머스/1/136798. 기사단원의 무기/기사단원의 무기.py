# 기사 1 ~number

def solution(number, limit, power):
    # 약수 먼저 찾기
    measure = []
    
    # 시간 초과가 나는 부분
    for i in range(1,number+1):
        m_count = 0
        for j in range(1,int(i ** (1/2))+1):
            if i % j == 0:
                if j * j == i:
                    m_count += 1
                else:
                    m_count += 2
        measure.append(m_count)
    
    #
    for i in range(number):
        if measure[i] > limit:
            measure[i] = power
    
    return sum(measure)