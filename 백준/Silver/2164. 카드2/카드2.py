from collections import deque

N = int(input())
queue = deque([])
if(N == 1):
    print(1)
else:
    for i in range(2,N+1,2):
        queue.append(i)
    # 홀수일때
    if(N%2 == 1):
        queue.appendleft(N)
        
    # 맨 앞에 수 제거 & 뒤에 오는 수 맨뒤로 보냄
    while(len(queue) > 1):
        queue.popleft()
        queue.append(queue[0])
        queue.popleft()
        
    print(queue[0])