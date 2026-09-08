def solution(hp):
    answer = 0
    # 장군개미 5 공격력
    answer += hp // 5
    hp %= 5
    
    # 병정개미 3 공격력
    answer += hp // 3
    hp %= 3
    
    # 일개미 1 공격력
    answer += hp // 1
    
    return answer