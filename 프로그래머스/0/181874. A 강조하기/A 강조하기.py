def solution(myString):
    m = myString.replace(myString,myString.lower())
    m = m.replace("a","A");
    return m