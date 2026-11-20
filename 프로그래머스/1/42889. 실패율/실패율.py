# 실패율을 구하는 코드 완성하기
# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

# count함수를 사용하면 매 반복문마다 해당 원소의 개수가 얼마인지를 확인하는데 그럴 필요없이 처음에 다 세고 나중에 조회하면 된다. 연산의 수가 줄어든다.
from collections import Counter

def solution(N, stages):
    rates = {} # 스테이지번호: 실패율
    length = len(stages) # 게임을 이용하는 전체 사용자의 수 

    counter = Counter(stages)    
    
    # 스테이지번호와 실패율을 함께 포함한 배열 추가
    for i in range(1,N+1):
        if length == 0 :
            rates[i] = 0 # 도달한 사람이 없는 경우 실패율 0
        else:
            rates[i] = counter[i] / length 
        length -= counter[i]
        
    # 실패율 기준 내림차순 정렬
    return sorted(rates.keys(), key=lambda x:rates[x],reverse=True)

