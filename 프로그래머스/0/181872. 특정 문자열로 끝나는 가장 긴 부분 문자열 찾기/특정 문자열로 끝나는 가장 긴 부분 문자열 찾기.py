def solution(myString, pat):
    # 목적 : myString에서 pat으로 끝나는 가장 긴 부분 문자열 찾기
    # 접근
    # 1. 맨 뒤에서부터 pat을 찾는다.
    # 2. 처음부터 해당 인덱스에다가 len(pat)을 더한값을 문자열 슬라이싱 한다.
    
    for i in range(len(myString)-len(pat),-1,-1):
        # 뒤에서부터 찾고 pat을 찾은 경우
        if myString[i:i+len(pat)] == pat:
            return (myString[:i+len(pat)])
            
    
    
    