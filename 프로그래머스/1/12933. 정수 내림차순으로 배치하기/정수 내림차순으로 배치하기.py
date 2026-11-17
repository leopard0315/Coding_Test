def solution(n):
    N = list(str(n))
    N.sort(reverse=True)
    return int(''.join(N))