# 실패율을 구하는 코드 완성하기
# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):
    result = [] # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열
    dict = {}
    length = len(stages) # 게임을 이용하는 전체 사용자의 수 
    
    stages.sort()
    
    # 스테이지번호와 실패율을 함께 포함한 배열 추가
    for i in range(1,N+1):
        count = stages.count(i) # 해당스테이지에 도달한 사람수 체크하기
        if length == 0:
            dict[i] = 0 # 도달한 사람이 없는 경우 0으로 판정하기
        else:
            dict[i] = count / length # 항상 0으로 나눌때 해당 값이 0이 되어서 비정상적인 종료가 되지는 않는지 확인한다.
        length -= count

    # 실패율 기준 내림차순 정렬한 새로운 배열 생성
    return sorted(dict.keys(), key=lambda x:dict[x],reverse= True)
