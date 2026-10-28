function solution(num_list){
    var sum = 0;
    var cross = 1; //곱셈을 사용할때는 기본값을 0이 아닌 1로 초기화시켜야한다.
    for(let i=0; i<num_list.length; i++){
        sum += num_list[i];
        cross = cross * num_list[i];
    }
    sum = (sum ** 2);
    if(sum>cross){
        return 1;
    }
    else{
        return 0;
    }
}