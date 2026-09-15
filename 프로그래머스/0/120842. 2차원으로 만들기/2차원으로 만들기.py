# 배열을 슬라이싱해서 한 것을 배열째로 새로운 배열에 추가
def solution(num_list, n):
    result = []
    for i in range(0, len(num_list),n):
        result.append(num_list[i:i+n])
    return result