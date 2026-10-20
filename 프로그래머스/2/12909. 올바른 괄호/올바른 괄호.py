# 경우의 수
# (의 개수 == )의 개수 일때 return 출력 
# 1) 리스트안에 아무것도 없을때 ) 오는 경우 cut
# 2) 리스트안에 ( 개수와 )가 동일하지 않을때

def solution(s):
    a = []
    
    for i in s:
        if i == '(':
            a.append(0)
        else :
            # 리스트안에 (가 없는데 )가 먼저 오는 경우 / 아닌경우 pop()하기
            if len(a) == 0:
                return False
            else:
                a.pop()
    # (의 개수  == )의 개수일때 / 아닌경우 false return
    if len(a) == 0:
        return True
    else:
        return False