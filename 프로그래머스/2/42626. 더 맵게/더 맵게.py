import heapq
# 최소 힙 사용
def solution(scoville, K):
    count = 0
    # 리스트를 heap으로 변환
    heapq.heapify(scoville)
    
    while (scoville[0] < K):
        # 힙의 길이 검사하기
        if len(scoville) < 2 :
            return -1
        
        # 최소값1, 2을 꺼내기
        smallest1 = heapq.heappop(scoville)
        smallest2 = heapq.heappop(scoville)
    
        # 새로운 값 창조 & 힙에 넣기
        mix = smallest1 + smallest2 * 2
        heapq.heappush(scoville,mix)
        
        # 섞는 값 세기
        count += 1
    return count
    
    