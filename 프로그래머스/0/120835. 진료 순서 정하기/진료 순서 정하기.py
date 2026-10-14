def solution(emergency):
    # 정답 담을 배열 생성
    answer = []
    
    # emergency를 내림차순정렬한 새로운 배열 생성 -> 원본 보존
    e = sorted(emergency,reverse=True)
    
    # 원본 배열인 emergency 원소가 새롭게 생성된 배열e에서는 몇번째 인덱스에 있는지 확인
    # 인덱스는 0부터 시작하니까 + 1을 해준다.
    # answer에 원소 추가해준다.
    for i in emergency:
        answer.append(e.index(i)+1)
    
    # 정답 배열 반환
    return answer
        