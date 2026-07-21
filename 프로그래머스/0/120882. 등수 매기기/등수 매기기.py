def solution(score):
    score2 = sorted([sum(i) for i in score],reverse = True)
    rank = [score2.index(sum(i))+1 for i in score]
    
    return rank