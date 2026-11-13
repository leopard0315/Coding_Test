def solution(s):
    len_s = len(s)
    if len_s % 2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]