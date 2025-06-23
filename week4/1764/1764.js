const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const nameMap = new Map();

// 듣도 못한 사람 등록 (해시 맵에 저장)
for (let i = 1; i <= N; i++) {
  nameMap.set(input[i], true);
}

const result = [];

// 보도 못한 사람을 확인하며 듣보잡 판별
for (let i = N + 1; i <= N + M; i++) {
  const name = input[i];
  if (nameMap.has(name)) {
    result.push(name);
  }
}

result.sort();
console.log(result.length);
result.forEach(name => console.log(name));
