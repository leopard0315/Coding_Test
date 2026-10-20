def solution(arr):
    stk = []
    i = 0
    
    while(i < len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            if arr[i] == stk[-1]:
                stk.pop()
            else:
                stk.append(arr[i])
        i += 1
    return stk if stk else [-1]
