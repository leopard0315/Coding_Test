def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row_result = []
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr2)):
                total += arr1[i][k] * arr2[k][j]
            row_result.append(total)
        answer.append(row_result)
    return answer