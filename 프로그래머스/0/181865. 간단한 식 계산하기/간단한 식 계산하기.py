def solution(binomial):
    # 정답을 담을 변수 초기화
    answer = 0
    
    # binomial의 숫자랑 연산자사이의 공백 제거 -> replace사용
    binomial_1 = binomial.replace(' ','')
    
    # if문으로 +,-,*이 있는지 구분하기
    if '+' in binomial_1:
        b_1 = binomial_1.split('+')
        answer = int(b_1[0]) + int(b_1[1])
        
    elif '-' in binomial_1:
        b_1 = binomial_1.split('-')
        answer = int(b_1[0]) - int(b_1[1])
        
    elif '*' in binomial_1:
        b_1 = binomial_1.split('*')
        answer = int(b_1[0]) * int(b_1[1])
    
    # 정답 반환
    return answer
            