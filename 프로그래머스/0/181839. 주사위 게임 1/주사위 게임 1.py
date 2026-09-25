def solution(a, b):
    # 1) a 와 b 모두 홀수일때
    if a % 2 == 1 and b % 2 == 1:
        return a ** 2 + b ** 2
    # 2) a와 b 모두 홀수가 아닐때
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a-b)
    else:
        return 2 * (a+b)