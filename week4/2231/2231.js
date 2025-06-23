const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString().trim());

let answer = 0;

// 1부터 N까지 모든 수를 탐색
for (let i = 1; i < N; i++) {
  const sum = i + String(i).split('').map(Number).reduce((a, b) => a + b, 0);

  // 만약 분해합이 입력값 N과 같다면, i는 N의 생성자
  if (sum === N) {
    answer = i; // 가장 먼저 발견된 생성자가 가장 작은 생성자
    break;
  }
}

console.log(answer); // 없으면 0 출력
