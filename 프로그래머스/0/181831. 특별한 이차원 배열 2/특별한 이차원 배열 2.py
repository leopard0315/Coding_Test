def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            # 만약 arr[i][j]랑 arr[j][i]가 다르다면, return 0 반환하고 아니라면 반복문을 전부 다 돌고 1을 반환하게 된다.(arr배열 내에서 전부 만족해야 1이고 하나라도 만족 못하면 0반환해야한다.)
            if arr[i][j] != arr[j][i]:
                return 0      
    return 1