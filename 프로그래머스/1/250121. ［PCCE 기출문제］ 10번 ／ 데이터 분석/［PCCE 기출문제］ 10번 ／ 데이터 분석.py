def solution(data, ext, val_ext, sort_by):
    answer = []
    # ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
    # 딕셔너리 사용해서 배열의 인덱스 값 저장
    a = {'code': 0, 'date': 1, 'maximum':2, 'remain':3}
    
    for i in data:
        if i[a[ext]] < val_ext:
            answer.append(i)
    
    answer.sort(key=lambda x: x[a[sort_by]])
            
    return answer