# 실패율을 구하는 코드 완성하기
# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):
    result = []
    answer = []
    length = len(stages) # 게임을 이용하는 전체 사용자의 수 
    stages.sort()
    
    for i in range(1,N+1):
        count = stages.count(i)
        if length == 0:
            answer.append((i,0))
        else:
            answer.append((i,count/length))
        length -= count

    answer.sort(key = lambda x: -x[1])

    for i in answer:
        result.append(i[0])
        
    return result
        
