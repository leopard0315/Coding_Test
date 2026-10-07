def solution(intStrs, k, s, l):
    answer = [] 
    # intStrs안에 있는 원소마다 각 문자열 슬라이싱 적용(s번 인덱스부터 l만큼의 크기)
    for i in intStrs:
        if int(i[s:s+l]) > k:
            answer.append(int(i[s:s+l]))
    return answer