def solution(strArr):
    # 딕셔너리 생성
    answer = {}
    # 
    for i in strArr:
        if len(i) in answer:
            answer[len(i)] += 1
        else:
            answer[len(i)] = 1
    # 딕셔너리의 value값을 기준으로 내림차순 정렬
    ans = sorted(answer.items(), key= lambda x:x[1],reverse = True)
    return ans[0][1]