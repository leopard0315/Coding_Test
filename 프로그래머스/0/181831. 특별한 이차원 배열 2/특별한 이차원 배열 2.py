def solution(arr):
    answer = -1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer = 1
            else:
                answer = 0
                break
        if answer == 0:
            break
                
    return answer