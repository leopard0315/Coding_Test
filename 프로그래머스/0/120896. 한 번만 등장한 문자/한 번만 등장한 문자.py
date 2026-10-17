def solution(s):
    # 접근
    # 1. count함수를 써서 원소 등장횟수 파악
    # 2. 해당 원소가 횟수가 1이라면 answer원소에 추가한다.
    # 3. answer를 오름차순 정렬한다.
    
    # 빈배열 생성
    answer = []
    
    # count함수의 결과값이 1이면 answer에 해당 원소 추가
    for i in s:
        if s.count(i) == 1:
            answer.append(i)
            
    # answer를 오름차순 정렬
    answer.sort()
    
    # 정렬된 answer를 문자열로 합친다.
    return ''.join(answer)
    
            
            