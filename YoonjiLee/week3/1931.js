//회의실 배정 문제
//끝나는 시간이 빠른 것 부터 정렬

const fs = require("fs");
const input = fs.readFileSync("run.txt").toString().trim().split("\n");

const n = Number(input[0]);
const meetings = input.slice(1).map((line) => {
  const [start, end] = line.split(" ").map(Number);
  return [start, end];
});

// 끝나는 시간 기준으로 정렬, 끝나는 시간이 같다면 시작 시간 기준
meetings.sort((a, b) => {
  if (a[1] === b[1]) return a[0] - b[0];
  return a[1] - b[1];
});

let count = 0;
let endTime = 0;

for (let i = 0; i < n; i++) {
  const [start, end] = meetings[i];
  if (start >= endTime) {
    count++;
    endTime = end;
  }
}

console.log(count);
