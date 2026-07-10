def solution(array, n):
    array.sort() # 일단 array 정렬
    for i in range(len(array)):
        if array[i] < n:
            continue
        else :
            # array안에 수보다 작은 경우
            if i == 0: 
                return array[0]
            
            if abs(array[i] - n) >= abs(n-array[i-1]):
                return array[i-1]
            else:
                return array[i]        
    # array안에 수보다 큰 경우
    return array[-1]