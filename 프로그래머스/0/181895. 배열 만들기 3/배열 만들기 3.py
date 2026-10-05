def solution(arr, intervals):
    # 1. 빈배열 생성
    answer = []
    # 2. 구간별로 x,y로 해서 변수 초기화
    x1 = intervals[0][0]
    x2 = intervals[1][0]
    y1 = intervals[0][1]
    y2 = intervals[1][1]
    
    # 3. 구간에 따른 각 인덱스의 값들을 answer배열에 추가하기
    # 3-1. 첫번째 구간 인덱스의 원소들 추가
    for i in range(x1,y1+1):
        answer.append(arr[i])
    # 3-2. 두번째 구간 인덱스의 원소들 추가
    for j in range(x2,y2+1):
        answer.append(arr[j])
    
    # 4. 정답 배열 반환
    return answer