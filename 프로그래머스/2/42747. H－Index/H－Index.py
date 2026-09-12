# 목표 : 과학자의 생산성과 영향력을 나타내는 지표인 H-index : h구하기
# 논문 n편 중에서 h번이상 인용된 논문이 h편이상이다.
# -> citations[i] >= (i+1)을 만족하는가? => 만족못할시 그 직전의 값 출력
# 예외) 만약 동일한 값들로만 이루어져있는경우 -> 배열의 길이 출력
def solution(citations):
    c = citations
    c.sort(reverse = True)
    for i in range(len(c)):
        if c[i] >= (i+1):
            continue
        else:
            return i
    return len(c)