def solution(my_string, indices):
    # 문자열 -> 리스트 변환
    my_list = list(my_string)
    
    # indices 정수배열을 내림차순으로 정렬
    indices.sort(reverse=True)
    
    # 리스트에서 해당하는 원소 제거하기
    for i in indices:
        my_list.pop(i)
    
    # 흩어진 리스트를 한개의 문자열로 합치기(join)
    return ''.join(my_list)