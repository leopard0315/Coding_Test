def solution(arr, flag):
    # 아이디어 : flag[i]가 true라면 arr[i] 값 * 2번 만큼 추가, flag[i]가 false라면 arr[i] 개만큼 뒤에서 원소 제거
    
    # 빈 배열 생성
    X = []
    
    # flag[i]가 true인 경우 ->  arr[i]를 arr[i] * 2만큼 추가하기
    # flag[i]가 false인 경우 -> arr[i] 개수만큼 x배열 끝에서 빼기 
    for i in range(len(flag)):
        if flag[i] == True:
            X.extend([arr[i]] * arr[i] * 2) # extend()는 만약 배열이라면, 배열안에 원소들만을 추가해서 넣어준다.
        else:
            # arr[i]개 만큼 뒤에서 원소 제거(1. pop()반복, 2. 문자열 슬라이싱 이용)
            del X[len(X)-arr[i]:]
 
    # X배열 반환하기
    return X