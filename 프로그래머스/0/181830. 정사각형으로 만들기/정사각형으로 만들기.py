def solution(arr):
    # 행의 길이 len(arr)
    # 열의 길이 len(arr[0])
    
    # 행의 수가 더 많은 경우
    if len(arr) > len(arr[0]):
        k = len(arr) - len(arr[0])
        for i in range(len(arr)):
            arr[i].extend([0]*k)
    # 열의 수가 더 많은 경우
    elif len(arr[0]) > len(arr):
        k = len(arr[0]) - len(arr)
        for i in range(k):
            arr.append([0] * len(arr[0]))
        
    # 행의 수와 열의 수가 동일한 경우 그대로 출력
    else:
        pass
    
    # 정답 반환
    return arr
