def solution(arr, idx):
    # 인덱스가 없다면 기본값 -1 반환
    answer = -1
    
    # for문을 idx부터 시작해서 배열 끝까지 돌리고
    # 조건에 맞는 값을 찾으면 break로 반복문 탈출(의미없는 반복 그만둠)
    for i in range(idx,len(arr)):
        if arr[i] == 1:
            answer = i
            break
    
    # 정답 코드 출력
    return answer