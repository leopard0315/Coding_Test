function solution(a, b) {
    var answer = 0;
    var answer1 = String(a) + String(b);
    if (Number(answer1)>= 2*a*b){
        return Number(answer1);
    }
    else{
        return 2*a*b;
    }
}