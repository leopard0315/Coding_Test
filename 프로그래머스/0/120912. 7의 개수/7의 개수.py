def solution(array):
    answer = 0
    for i in array:
        cnt = str(i).count('7')
        answer += cnt
    return answer