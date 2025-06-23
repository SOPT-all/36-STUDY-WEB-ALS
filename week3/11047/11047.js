const fs = require('fs'); 
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K] = input[0].split(' ').map(Number);
const coins = input.slice(1).map(Number); // 동전 종류 배열로 저장

coins.sort((a, b) => b - a);

let remaining = K;  
let count = 0;     // 동전 개수 누적용 변수

for (let i = 0; i < N; i++) { 
  const coin = coins[i]; 
  if (coin <= remaining) { 
    const num = Math.floor(remaining / coin); // 현재 동전으로 만들 수 있는 최대 개수
    remaining -= num * coin; // 남은 금액에서 현재 동전으로 만든 금액을 뺌
    count += num;            // 동전 개수 누적
  }
}

console.log(count);