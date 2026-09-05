def solution(i, j, k):
    answer = sum([str(a).count(str(k)) for a in range(i,j+1)])
    return answer