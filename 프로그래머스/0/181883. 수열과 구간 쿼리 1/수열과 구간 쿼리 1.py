def solution(arr, queries):
    # 0. 빈 배열 생성
    answer = []
    # 1. queries의 각 원소를 추출
    # 2. 원소의 첫번째 원소가 s, 두번째원소가 e이므로 j가 s랑 e사이에 존재하는 arr[j]에 대해 1씩 증가해주기
    for i in queries:
        for j in range(i[0],i[1]+1):
            arr[j] += 1
    
    # 3. 정답 배열 반환
    return arr