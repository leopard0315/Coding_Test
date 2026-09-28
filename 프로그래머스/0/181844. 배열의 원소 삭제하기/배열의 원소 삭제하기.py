def solution(arr, delete_list):
    # arr에 속하지만, 동시에 delete_list 원소에는 존재하지않는 요소들의 순서를 그대로 유지한 배열 출력
    answer = [i for i in arr if i not in delete_list]
    return answer