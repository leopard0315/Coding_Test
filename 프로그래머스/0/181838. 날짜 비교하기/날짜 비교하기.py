def solution(date1, date2): # [year,month,day]
    # 정수배열 date1과 date2로 쪼개기
    year1, month1, day1 = date1
    year2, month2, day2 = date2

    # 1. 연도가 작으면 1 반환
    if year1 < year2:
        return 1
    # 2. 연도가 같고 월이 작은 경우 1반환
    elif year1 == year2 and month1 < month2:
        return 1
    # 3. 연도가 같고 월이 같은 경우, 일이 작은 경우 1 반환
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return 1
    # 4. 나머지 경우 전부 0반환
    else:
        return 0
