import heapq

def solution(n, works):
    answer = 0
    heap = []
    works = [-x for x in works]
    heapq.heapify(works)
    
    for _ in range(n):
        # 가장 큰 원소빼기
        num = heapq.heappop(works)
        # 1 감소하는데 0인경우 return
        if num == 0:
            return 0
        else:
            num += 1
        # 해당값을 다시 힙에 추가
        heapq.heappush(works,num)
    
    for i in works:
        answer += i ** 2
    return answer