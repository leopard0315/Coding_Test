def solution(n_str):
    n = 0
    for i in range(len(n_str)):
        if n_str[i] == '0':
            continue
        else:
            n = i
            break
        
    return n_str[n:]