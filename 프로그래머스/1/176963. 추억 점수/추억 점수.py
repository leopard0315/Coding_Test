def solution(name, yearning, photo):
    result = []
    for i in photo:
        total = 0
        for j in range(len(name)):
            if name[j] in i:
                total += yearning[j]
        result.append(total)
    return result
                
 
