# 사과 점수 : 1 ~ k
# 한상자에 m개씩 포장
# 가장 낮은 점수 p인 경우 -> p * m
def solution(k, m, score):
    total = 0
    score.sort(reverse=True)

    for i in range(0,len(score),m):
        if len(score[i:i+m]) == m:
            total += min(score[i:i+m]) * m
    return total