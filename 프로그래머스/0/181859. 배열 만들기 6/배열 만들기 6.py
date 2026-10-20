def solution(arr):
    # 빈배열, i 생성 및 초기화
    stk = []
    i = 0
    
    # i가 len(arr)가 작은 경우 반복
    while(i < len(arr)):
        # stk가 빈배열인 경우, stk에 원소 추가
        if len(stk) == 0:
            stk.append(arr[i])
        # stk가 빈배열이 아닌 경우 
        else:
            # stk의 마지막 원소 = arr[i] 인 경우, stk의 마지막 원소 제거
            if arr[i] == stk[-1]:
                stk.pop()
            # stk의 마지막 원소 != arr[i]인 경우, stk의 원소 추가
            else:
                stk.append(arr[i])
        # 어떤 경우에 따라 i += 1이다.
        i += 1
    # stk가 빈배열인 경우, [-1]반환하고 아니면 stk반환
    return stk if stk else [-1]
