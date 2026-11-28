# 왼쪽에 더 큰수, 오른쪽에 더 작은 수 - 통일 시킨다.
def solution(sizes):
    answer = 0
    Max1, Max2 = 0 , 0
    for w,h in sizes:
        if w < h:
            w, h = h, w
        
        if Max1 < w:
            Max1 = w
        if Max2 < h:
            Max2 = h   
    
    return Max1 * Max2