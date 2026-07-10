def solution(n):
    answer = 1
    j = 1
    for i in range(2,11):
        if answer <= n:
            answer *= i
            j += 1
        else:
            return j-1
    return j