def solution(absolutes, signs):
    # 정수들의 절댓값들의 배열 absolutes
    # 정수들의 배열 signs
    total = 0
    for i in range(len(signs)):
        if signs[i] == True:
            total += absolutes[i]
        else:
            total -= absolutes[i]
    return total