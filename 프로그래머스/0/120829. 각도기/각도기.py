def solution(angle): # 예각,직각,둔각,평각
    answer = 0
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle == 180:
        answer = 4
    else:
        answer = 3
    return answer