# 목표 : 과학자의 생산성과 영향력을 나타내는 지표인 H-index : h구하기
def solution(citations):
    c = citations
    c.sort(reverse = True)
    for i in range(len(c)):
        if c[i] >= (i+1):
            continue
        else:
            return i
    return len(c)