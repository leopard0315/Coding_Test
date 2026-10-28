function solution(num_list) {
    for(let i =num_list.length-1; i > num_list.length-2; i--){
        if(num_list[i] > num_list[i-1]){
            num_list[i+1] = num_list[i] - num_list[i-1];
        }
        else{
        num_list[i+1] = num_list[i]*2;
        }
    }
    return num_list;
}