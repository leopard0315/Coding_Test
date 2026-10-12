def solution(arr, flag):
    # 아이디어 : flag[i]가 true라면 arr[i] 값 * 2번 만큼 추가, flag[i]가 false라면 arr[i] 개만큼 뒤에서 원소 제거
    
    # 빈 배열 생성
    X = []
    
    # flag[i]가 true인 경우 ->  arr[i]를 arr[i] * 2만큼 추가하기
    # flag[i]가 false인 경우 -> arr[i] 개수만큼 x배열 끝에서 빼기 
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i] * 2):
                X.append(arr[i])
        elif flag[i] == False:
            for j in range(arr[i]):
                X.pop() 
 
    # X배열 반환하기
    return X