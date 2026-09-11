def solution(array, commands):
    answer = []
    for i in commands:
        # 배열 슬라이싱
        new_list = array[i[0]-1:i[1]]
        
        # 정렬
        new_list.sort()
        
        # 원소 추가
        answer.append(new_list[i[2]-1])
    return answer