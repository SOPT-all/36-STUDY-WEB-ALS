//하노이탑
const fs = require("fs");
const input = +fs.readFileSync("run.txt").toString().trim();
let result = [];
let count = 0;

function hanoi(n, from, to, via) {
  if (n === 1) {
    result.push(`${from} ${to}`);
    count++;
    return;
  }

//문제 작게 쪼개기 -> 분할정복
  hanoi(n - 1, from, via, to); // 1단계: n-1개를 보조 기둥으로
  result.push(`${from} ${to}`); // 2단계: 가장 큰 원판을 목표 기둥으로
  count++;
  hanoi(n - 1, via, to, from); // 3단계: 보조 기둥에 있던 n-1개를 목표 기둥으로
}

hanoi(input, 1, 3, 2);

console.log(count);
console.log(result.join("\n"));
