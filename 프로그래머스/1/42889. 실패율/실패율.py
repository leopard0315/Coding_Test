# 실패율을 구하는 코드 완성하기
# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):
    result = [] # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열
    answer = [] #
    length = len(stages) # 게임을 이용하는 전체 사용자의 수 
    
    
    for i in range(1,N+1):
        count = stages.count(i)
        if length == 0:
            answer.append((i,0))
        else:
            answer.append((i,count/length)) # 항상 0으로 나눌때 해당 값이 0이 되어서 비정상적인 종료가 되지는 않는지 확인한다.
        length -= count

    # 실패율 기준 내림차순 정렬
    answer.sort(key = lambda x: -x[1])

    # 스테이지 번호만 뽑기
    for i in answer:
        result.append(i[0])
        
    return result
        
