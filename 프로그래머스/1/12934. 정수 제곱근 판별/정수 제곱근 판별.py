def solution(n):
    ans = 1
    for i in range(n):
        if ans ** 2 == n:
            return (ans + 1) ** 2
        else:
            ans += 1
    return -1