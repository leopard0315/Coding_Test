def solution(picture, k):
    # 빈 배열 생성
    answer = []
    
    # 각 원소를 꺼내서 리스트로 타입변경
    for i in picture:
        arr = list(i)
        # 해당 원소의 원소를 1개씩 뽑아서 가로롤 k만큼 길이 증가
        for j in range(len(arr)):
            arr[j] = arr[j] * k
        
        # 구한 리스트를 문자열로 합치고 세로의 길이를 k만큼 길이 증가
        for _ in range(k):
            answer.append(''.join(arr))
    
    # 가로k만큼 늘어난 배열과 세로k만큼 늘어난 배열을 반환한다.
    return answer