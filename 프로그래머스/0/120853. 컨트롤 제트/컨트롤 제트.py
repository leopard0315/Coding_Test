def solution(s):
    answer = 0
    # 공백을 쪼갠다.
    a = s.split(' ')
    
    # 해당 배열에서 'Z'라면 이전 원소를 뺀다. (<- Z가 연속되어있지않기 때문에)
    # 해당 배열에서 'Z'가 아니라면 해당 원소인 숫자를 더한다.
    for i in range(len(a)):
        if a[i] == 'Z':
            answer -= int(a[i-1])
        else:
            answer += int(a[i])
    
    # 정답 반환
    return answer