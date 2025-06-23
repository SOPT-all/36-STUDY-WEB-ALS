const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

let N = parseInt(input); // 총 설탕 무게
let count = 0; // 봉지 개수 카운트

while (true) {
  if (N % 5 === 0) {
    count += N / 5;
    console.log(count);
    break;
  }

  // 3kg을 한 번 빼서 남은 무게가 나눠떨어지는지
  N -= 3; 
  count += 1; 

  // N이 음수면 → -1 출력
  if (N < 0) { 
    console.log(-1); 
    break;
  }
}
