def solution(myString, pat):
    # 목적 : myString에서 pat으로 끝나는 가장 긴 부분 문자열 찾기
    # 접근
    # 1. 맨 뒤에서부터 pat을 찾는다.
    # 2. 처음부터 해당 인덱스에다가 len(pat)을 더한값을 문자열 슬라이싱 한다.
    
    # 맨 뒤에서 pat의 길이를 뺀 인덱스부터 0인덱스까지 -1씩 감소 반복
    for i in range(len(myString)-len(pat),-1,-1):
        # 문자열을 뒤에서부터 찾고 처음으로 pat을 찾은 경우
        if myString[i:i+len(pat)] == pat:
            return (myString[:i+len(pat)])
            
    
    
    