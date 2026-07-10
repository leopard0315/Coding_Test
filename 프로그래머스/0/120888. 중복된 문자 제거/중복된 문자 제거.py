def solution(my_string):
    a = list(my_string)
    b = set()
    answer = ''
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.add(a[i])
            answer += a[i]
    return answer
    