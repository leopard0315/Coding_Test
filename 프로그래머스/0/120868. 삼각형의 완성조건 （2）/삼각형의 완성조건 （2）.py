def solution(sides):
    # 1) sides를 정렬한다. a < b
    # 2-1) 가장 긴변이 새로 들어오는 수인 경우 : a < b < x -> a + b > x
    # 2-2) a < x < b 인 경우
    # 2-3) x < a < b인 경우
    answer = 0
    side = sorted(sides)
    # 정렬
    for i in range(sides[1]-sides[0]+1,sides[0]+sides[1]):
        side = sorted(sides)
        side.append(int(i))
        side.sort()
        if side[0] + side[1] > side[2]:
            answer +=1
    return answer
        