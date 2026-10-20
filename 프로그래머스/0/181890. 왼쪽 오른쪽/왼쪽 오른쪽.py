def solution(str_list):
    # 접근
    # 1. 가장 먼저 'l' or 'r' 이 있는지 확인
    # 2. 'l' or 'r' 중에 'l'이 먼저 나오면 l기준으로 왼쪽 문자열들을 순서대로 담은 리스트
    # 2-2. 'r'이 먼저 나오면 r기준으로 오른쪽 문자열들을 순서대로 담은 리스트
    
    # 문자는 index를 기준으로 index가 누가 더 작은지 비교해서 구한다.
    str1 = ''.join(str_list)
    # l,r이 모두 있는 경우
    if 'l' in str1 and 'r' in str1:
        L = str1.index('l')
        R = str1.index('r')
        if L < R :
            return list(str1[:L]) 
        else:
            return list(str1[R+1:])
        
    elif 'l' in str1:
        L = str1.index('l')
        return list(str1[:L])
    elif 'r' in str1:
        R = str1.index('r')
        return list(str1[R+1:])
    else:
        return []
        
        
