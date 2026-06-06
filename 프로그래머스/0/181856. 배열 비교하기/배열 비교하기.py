def solution(arr1, arr2):
    answer = 0
    # 배열의 길이가 다를때
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    else: # 배열의 길이가 같을때
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
        
        
    return answer