# 경우의 수
# 1) 리스트안에 아무것도 없을때 ) 오는 경우 cut
# 2) 리스트안에 ( 개수와 )가 동일하지 않을때

def solution(s):
    a = []
    
    for i in s:
        if i == '(':
            a.append('(')
        else :
            if len(a) == 0:
                return False
            else:
                a.pop()
    if len(a) == 0:
        return True
    else:
        return False