# 로또 당첨의 최저 순위와 최고 순위 알아보기
# 알아볼 수 없는 수: 0
def solution(lottos, win_nums):
    result = []
    overlap = set(lottos) & set(win_nums)

    Min = len(overlap)
    Max = lottos.count(0) + Min
    
    array = [Max,Min]
    
    for i in array:
        if i == 6:
            result.append(1)
        elif i == 5:
            result.append(2)
        elif i == 4:
            result.append(3)
        elif i == 3:
            result.append(4)
        elif i == 2:
            result.append(5)
        else:
            result.append(6)
    
    return result