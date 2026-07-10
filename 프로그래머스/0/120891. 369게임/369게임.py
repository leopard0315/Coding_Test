def solution(order):
    order = str(order)
    answer = 0
    for i in order:
        if i == '3' or i == '6' or i == '9':
            answer += 1
    return answer