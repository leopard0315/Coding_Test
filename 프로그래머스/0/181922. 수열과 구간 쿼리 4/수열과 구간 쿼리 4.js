function solution(arr, queries) {
    arr = [];
    for(let a=0; a<queries.length; a++){
        for(let i=queries[a][0]; i<=queries[a][1]; i++){
            if(i%queries[a][2] ==0){
                arr[i] += 1
            }
        }
    }
    return arr;
}