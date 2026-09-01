def solution(dot):
    answer = 0
    x = dot[0]
    y = dot[1]
    if x > 0 :
        if y > 0:
            return 1
        elif y < 0 :
            return 4
    else:
        if y > 0 :
            return 2
        else:
            return 3
            