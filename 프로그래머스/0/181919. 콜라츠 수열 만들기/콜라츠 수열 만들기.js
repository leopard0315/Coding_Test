function solution(n,answer = []) {
    answer.push(n)
    if(n==1) return answer;
    if(n%2==0) return solution(n/2,answer)
    else return solution(n*3 +1,answer)
    
    /*
    while(n>1){
        answer.push(n)
        if(n%2==0){
            n = n/2;
        }
        else{
            n = 3*n + 1;
        }

    }
    answer.push(n)
    
    return answer;
    */
}