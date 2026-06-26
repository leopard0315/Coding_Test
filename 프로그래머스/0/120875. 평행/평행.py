def solution(dots):
    answer = 0
    x1,y1 = dots[0][0], dots[0][1]
    x2,y2 = dots[1][0], dots[1][1]
    x3,y3 = dots[2][0], dots[2][1]
    x4,y4 = dots[3][0], dots[3][1]
    
    # 1-2,3-4
    if (abs(x2-x1) * abs(y4-y3)) == (abs(x4-x3) * abs(y2-y1)):
        answer = 1
    # 1-3,2-4
    elif (abs(x3-x1) * abs(y4-y2)) == (abs(x4-x2) * abs(y3-y1)):
        answer = 1
    elif (abs(x4-x1) * abs(y3-y2)) == (abs(x3-x2) * abs(y4-y1)):
        answer = 1
    else :
        answer = 0
    
    return answer