def solution(date1, date2): # [year,month,day]
    # 정수배열 date1과 date2로 쪼개기
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    
    # 1. 연도가 같거나 작은지 판단
    # 2. 월이 같거나 작은지 판단
    # 3. 일이 작은지 판단
        # 3-1. 작다면 1 반환
        # 3-2. 해당 조건에 만족하지않는다면 전부 0반환
    if year1 < year2:
        return 1
    elif year1 == year2 and month1 < month2:
        return 1
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return 1
    else:
        return 0
