def solution(s):
    # 올바른 괄호 : True, 올바르지않은 괄호 : False
    count = 0 # '('가 추가되면 +1, ')'이 추가되면 -1
    
    for i in s:
        # 1. count값이 0이하인데 ')'가 들어오는 경우
        if count <= 0 and i == ')':
            return False
        # 2. '('이 추가된 경우 +1 증가
        if i == '(':
            count += 1
        # 3. 이전 원소가 '('인데, 현재 원소가 ')'인 경우 -1 감소
        if count > 0 and i == ')':
            count -= 1
    
    # count값이 0이라면 True, 아니라면 False반환
    return True if count == 0 else False 
    