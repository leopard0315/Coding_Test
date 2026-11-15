def solution(a, b):
    answer = 0
    m = min(a,b)
    M = max(a,b)
    
    return sum(range(m,M+1))