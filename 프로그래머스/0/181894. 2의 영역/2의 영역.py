def solution(arr):
    ## 배열안의 2가 모두 포함하면서 가장 작은 연속된 부분배열 = 2를 모두 포함하면서 양쪽 끝이 2로 이루어진 경우
    # arr에 2가 없는 경우 -> [-1] 반환
    if 2 not in arr:
        return [-1]
    # 배열안의 2가 처음으로 나오는 곳에서부터 뒤에서 처음으로 2가 나오는곳까지 반환
    else:
        return arr[arr.index(2): len(arr) - arr[::-1].index(2)]