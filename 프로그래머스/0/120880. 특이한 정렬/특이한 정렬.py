def solution(numlist, n):
    answer = []
    diff = []
    for i in numlist:
        diff.append(abs(n-i))
    arr = zip(numlist,diff)
    arr = list(arr)
    arr.sort(key=lambda x:(x[1],-x[0]))
    for j in arr:
        answer.append(j[0])
    return answer