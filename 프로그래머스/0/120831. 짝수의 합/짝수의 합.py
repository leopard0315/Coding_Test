def solution(n):
    answer = 0
    if (n%2 != 0): # 홀수일때
        n -= 1
    for i in range(n,0,-2):
        answer += i
    return answer