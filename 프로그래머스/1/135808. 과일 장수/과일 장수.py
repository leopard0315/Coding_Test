# 사과 점수 : 1 ~ k
# 한상자에 m개씩 포장
# 가장 낮은 점수 p인 경우 -> p * m
# 내림차순 정렬한다음에 리스트를 m만큼 나누어서 구한다. 이때 남은 리스트의 길이가 m보다 작다면 패스한다.
def solution(k, m, score):
    # 최대이익변수 생성
    total = 0
    
    # 내림차순 정렬
    score.sort(reverse=True)

    # 리스트를 m만큼 자르고 남은 리스트의 길이가 m보다 작으면 컷한다.
    for i in range(0,len(score),m):
        if len(score[i:i+m]) == m:
            total += min(score[i:i+m]) * m
    
    # 정답 반환
    return total