function solution(str1, str2) {
    var answer = '';
    /*
    let j = 0;
    let k = 0;
    for(let i=0; i<(str1.length+str2.length); i++){
        if(i%2==0){ //짝수이면 str1의 요소 추가
            answer += str1[j];
            j = j+1;
        }
        else{
            answer += str2[k];
            k = k+1;
        }
    }
    */
    for(let i=0; i<str1.length; i++){
        answer += str1[i];
        answer += str2[i];
    }
    return answer;
}