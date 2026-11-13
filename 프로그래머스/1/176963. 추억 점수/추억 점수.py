def solution(name, yearning, photo):
    result = []
    # 2차원 배열 photo에서 각 배열의 요소(1차원 배열)을 빼낸다.
    for i in photo:
        total = 0
        # 1차원 배열에서 name에서 있는 요소가 있는지 확인 -> 있다면 해당 위치에 해당하는 yearning의 값을 더한다.
        for j in range(len(name)):
            if name[j] in i:
                total += yearning[j]
        result.append(total)
    return result
                
 
