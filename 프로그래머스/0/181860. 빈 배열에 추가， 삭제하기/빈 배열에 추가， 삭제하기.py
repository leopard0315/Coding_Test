def solution(arr, flag):
    # 아이디어 : flag[i]가 true라면 arr[i] 값 * 2번 만큼 추가, flag[i]가 false라면 arr[i] 개만큼 뒤에서 원소 제거
    
    X = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i] * 2):
                X.append(arr[i])
        elif flag[i] == False:
            for j in range(arr[i]):
                X.pop()   
    return X