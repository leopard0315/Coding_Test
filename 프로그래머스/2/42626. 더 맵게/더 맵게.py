# 최소 힙

# 리스트가 아닌 heap 상태로 만들어서 가장 맨앞에 작은값, 가장 뒤쪽에 큰값이 오도록 한다.
# 가장 큰 특징은 원소를 삽입시에 자동적으로 적재적소 자리에 들어간다는 점이다.
# [사용 방법]
# import heapq -라이브러리 
# heapq.heapify(list)  - list를 힙으로 변환
# 최솟값 꺼내기 - heapq.heappop(list)
# 원소 집어넣기 - heapq.heappush(list,넣고자하는 원소)

import heapq
# 최소 힙 사용
def solution(scoville, K):
    count = 0
    
    # 리스트를 heap으로 변환
    heapq.heapify(scoville)
    
    while (scoville[0] < K):
        # 예외처리 : 힙의 길이 검사하기
        if len(scoville) < 2 :
            return -1
        
        # 최소값1, 2을 꺼내기
        smallest1 = heapq.heappop(scoville)
        smallest2 = heapq.heappop(scoville)
    
        # 새로운 스코빌 지수 & 힙에 넣기
        mix = smallest1 + smallest2 * 2
        heapq.heappush(scoville,mix)
        
        # 섞는 값 세기
        count += 1
    return count
    
    