def solution(my_string):
    m = list(my_string.lower())
    m.sort()
    return "".join(m)
    