def solution(arr, intervals):
    # 1. 빈배열 생성
    answer = []
    # 2. 구간별로 x,y로 해서 변수 초기화
    x1 = intervals[0][0]
    x2 = intervals[1][0]
    y1 = intervals[0][1]
    y2 = intervals[1][1]
    
    # 3. 문자열 슬라이싱 이용해서 집어넣기
    answer = arr[x1:y1+1] + arr[x2:y2+1]
    
    # 4. 정답 배열 반환하기
    return answer