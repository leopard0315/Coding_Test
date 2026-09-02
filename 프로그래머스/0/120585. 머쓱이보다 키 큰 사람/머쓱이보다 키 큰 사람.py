def solution(array, height):
    array.append(height) # 머쓱이 키 추가
    array.sort(reverse = True) # 머쓱이 키를 추가한후에 거꾸로 정렬하고
    return array.index(height) # 해당 인덱스를 표현해서 뒤에서 몇번째인지 위치 구하기