def solution(array, commands):
    answer = []
    for components in commands:
        # 배열 슬라이싱
        i,j,k = components
        new_list = array[i-1:j]
        
        # 정렬
        new_list.sort()
        
        # 원소 추가
        answer.append(new_list[k-1])
    return answer