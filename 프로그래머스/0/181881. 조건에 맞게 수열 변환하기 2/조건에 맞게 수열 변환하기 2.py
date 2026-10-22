# 해당 작업을 change 함수형태로 만듦
# arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.
def change(arr):
    new_list = []
    for i in arr:
        if i >= 50:
            if i%2 == 0:
                new_list.append(i // 2)
            else:
                new_list.append(i)
        else:
            if i%2 == 1:
                new_list.append(i * 2 + 1)
            else:
                new_list.append(i)
    return new_list

# 바꾼 함수와 이전함수의 값이 동일한때의 x값 출력하기
def solution(arr):
    x = 0
    while(1):
        arr1 = change(arr)
        if arr == arr1:
            break
        else:
            x += 1
            arr = arr1
    return x 