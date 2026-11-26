# 필요한 물품 구매하고싶다.
# 전체 예산 한정 -> 최대한 많은 부서의 물품을 구매해줄 수 있도록 한다.
# 지원할거면 미달되게가 아닌 지원금액을 전부 지원해줘야한다.
def solution(d, budget):
    ans = 0
    d.sort()
    for i in range(len(d)):
        budget = budget - d[i]
        if budget >= 0:
           ans = i+1 
        else:
            break
    
    return ans