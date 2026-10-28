function solution(a, b) {
    var answer = 0;
    let answer1 = String(a) + String(b);
    let answer2 = String(b) + String(a);
    if(Number(answer1)>= Number(answer2)){
        return Number(answer1);
    }
    else{
        return Number(answer2);
    }
}