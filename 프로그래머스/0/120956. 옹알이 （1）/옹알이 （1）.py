def solution(babbling):
    answer = 0
    for i in babbling:
        length = len(i)
        count = 0
        # len(i) 길이가 10 / 8 / 7 / 6 / 5 / 4 / 3/ 2
        if length == 10:
            if 'aya' in i:
                if 'ye' in i:
                    if 'woo' in i:
                        if 'ma' in i:
                            count += 4
        elif length == 8: # 3 3 2
            if 'aya' in i:
                if 'woo' in i:
                    if 'ye' in i or 'ma' in i:
                        count += 3
        elif length == 7:
            if 'ye' in i:
                if 'ma' in i:
                    if 'woo' in i or 'aya' in i:
                        count +=3
        elif length == 6:
            if 'aya' in i:
                if 'woo' in i:
                    count += 2
        elif length == 5:
            if 'aya' in i or 'woo' in i:
                if 'ye' in i or 'ma' in i:
                    count+= 2
        elif length == 4:
            if 'ye' in i:
                if 'ma' in i:
                    count += 2
        elif length == 3:
            if 'aya' in i or 'woo' in i:
                count += 1
        elif length == 2:
            if 'ma' in i or 'ye' in i:
                count += 1

        if count != 0:
            answer += 1
    return answer