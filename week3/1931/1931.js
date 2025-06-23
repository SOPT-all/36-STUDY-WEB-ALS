const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);

const meetings = input.slice(1).map(line => line.split(' ').map(Number)); // 회의 시작 시간, 종료 시간 숫자로 변환

// 1. 회의를 끝나는 시간 기준으로 정렬
// 2. 끝나는 시간이 같을 경우 시작 시간 기준으로 정렬
meetings.sort((a, b) => { 
  if (a[1] === b[1]) return a[0] - b[0]; 
  return a[1] - b[1];
});

let count = 0;         // 회의 개수 카운트
let lastEndTime = 0;   // 마지막 회의 종료 시간

for (let i = 0; i < N; i++) {
  const [start, end] = meetings[i]; 
  
  if (start >= lastEndTime) {   // 회의 시작 시간이 마지막 종료 시간 이후라면 배정
    lastEndTime = end;  // 마지막 회의 종료 시간 업데이트
    count++; 
  }
}

console.log(count); 
