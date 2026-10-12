def solution(strArr):
    # 가장 큰 개수의 그룹의 크기 출력 -> max값 이용
    # 딕셔너리 생성
    answer = {}
    
    # 문자열의 길이의 딕셔너리 key값이 없다면 추가하고 있다면 1씩 증가한다.
    for i in strArr:
        if len(i) in answer:
            answer[len(i)] += 1
        else:
            answer[len(i)] = 1
            
    # 딕셔너리의 value값을 기준으로 내림차순 정렬
    ans = sorted(answer.items(), key= lambda x:x[1],reverse = True)
    
    # 가장 맨 앞(가장 큰 값)의 value값 반환
    return ans[0][1]