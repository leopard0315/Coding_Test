def solution(s):
    # 올바른 괄호 : True, 올바르지않은 괄호 : False
    stack = []
    
    for i in s:
        # 1. stack이 비어있는데 ')'가 들어오는 경우
        if len(stack) == 0 and i == ')':
            return False
        # 2. '('이 추가된 경우 - append()
        if i == '(':
            stack.append(i)
        # 3. 이전 원소가 '('인데, 현재 원소가 ')'인 경우 - pop()
        if i == ')' and stack[-1] == '(':
            stack.pop()
    
    # stack이 비어있다면 True, 아니라면 False반환
    return False if stack else True 
    