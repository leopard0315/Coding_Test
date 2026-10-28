function solution(my_string, k) {
    // 1) for문을 통해 해결
    /*
    var answer = '';
    for(let i =1; i<=k; i++){
        answer += my_string;
    }
    return answer;
    */   
    // 2) 단순 반복문 : repeat()를 사용해 해결 가능(반복하고자하는 문자열과 반복횟수가 주어질때)
    return my_string.repeat(k);
}