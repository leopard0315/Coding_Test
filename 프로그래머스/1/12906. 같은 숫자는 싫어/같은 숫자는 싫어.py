def solution(arr):
    answer = [] # queue
    answer.append(arr[0])
    if len(arr) == 1:
        pass
    else:
        for i in range(1,len(arr)):
            if arr[i] == answer[-1] :
                continue
            else:
                answer.append(arr[i])
    return answer        
            
                
    return answer