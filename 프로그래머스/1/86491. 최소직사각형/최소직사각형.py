# 왼쪽에 더 큰수, 오른쪽에 더 작은 수 - 통일 시킨다.
def solution(sizes):
    answer = 0
    Max1, Max2 = 0 , 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        
        if Max1 < sizes[i][0]:
            Max1 = sizes[i][0]
        if Max2 < sizes[i][1]:
            Max2 = sizes[i][1]    
    
    return Max1 * Max2