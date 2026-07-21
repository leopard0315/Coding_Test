def solution(score):
    score1 = []
    for i in range(len(score)):
        temp = 0
        for j in range(2):
            temp += score[i][j]
        
        score1.append(temp / 2)
    
    score2 = sorted(score1,reverse = True)
    rank = [score2.index(i)+1 for i in score1]
    
    return rank