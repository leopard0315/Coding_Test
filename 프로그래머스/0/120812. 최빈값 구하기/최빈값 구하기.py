def solution(array):
    mode = {}
    for i in range(len(array)):
        mode[array[i]] = array.count(array[i])
    
    print(mode)
    mode1 = list(sorted(mode.items(),key=lambda x:-x[1]))
    print(mode1)
    if len(mode1) >=2:
        if mode1[0][1] == mode1[1][1]:
            return -1
    return mode1[0][0]
