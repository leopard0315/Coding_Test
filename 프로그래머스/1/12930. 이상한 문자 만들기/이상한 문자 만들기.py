def solution(s):
    answer = []
    S = s.split(' ')
    for i in S:
        ans = ''
        for j in range(len(i)):
            if j % 2 == 0:
                ans += i[j].upper()
            else:
                ans += i[j].lower()
        answer.append(ans)
    return ' '.join(answer)