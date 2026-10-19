def solution(s):
    answer = 0
    a = s.split(' ')
    print(a)
    for i in range(len(a)):
        if a[i] == 'Z':
            answer -= int(a[i-1])
        else:
            answer += int(a[i])
    return answer