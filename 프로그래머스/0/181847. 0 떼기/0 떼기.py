def solution(n_str):
    n = 0
    for i in range(len(n_str)):
        if n_str[i] != '0':
            return n_str[i:]