function solution(code) {
    var ret = '';
    var mode = 0;
    for(let i=0; i<code.length; i++){
        if(mode == 0){ //모드가 0일때
            if(code[i] != "1"){
                if(i%2==0){ //짝수일때
                    ret += code[i];
                }
            }
            else {
                mode = 1;
            }
        }
        else{ //모드가 1일때
            if(code[i] != "1"){
                if(i%2==1){ //홀수일때 추가
                    ret += code[i];
                }
            }
            else{
                mode = 0;
            }
        }
    }
    if(ret == ''){
        return "EMPTY";
    }
    return ret;
}