function solution(arr, queries) {
    let result = [];
    
    queries.forEach(query => {
        const [s, e, k] = query;
        let min = Infinity;

        // s부터 e까지 범위를 순회하면서 k보다 큰 값 중 가장 작은 값을 찾음
        for (let i = s; i <= e; i++) {
            if (arr[i] > k && arr[i] < min) {
                min = arr[i];
            }
        }

        // min 값이 갱신되지 않았다면 -1을 추가, 그렇지 않으면 min 값을 추가
        result.push(min === Infinity ? -1 : min);
    });
    
    return result;
}
