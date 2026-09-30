def solution(wallet, bill):
    # 1. 지폐를 접은 횟수 저장 변수 answer
    answer = 0
    
    # 2. 반복문과 if문을 통해서 분기해서 조건에 따라 구함.
    while((min(bill) >  min(wallet)) or (max(bill) > max(wallet))):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill [1] = bill[1] // 2
        answer += 1
    
    # 3. answer값 리턴
    return answer