import heapq

def solution(n, works):
    answer = 0
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
    
    while(n!=0):
        n -= 1
        # 가장 큰 원소빼기
        num = -heapq.heappop(heap)
        # 1 감소하는데 0인경우 return
        if num == 0:
            return 0
        else:
            num -= 1
        # 해당값을 다시 힙에 추가
        heapq.heappush(heap,-num)
    
    for i in heap:
        answer += i ** 2
    return answer