const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// N: 상근이 카드 개수
const N = Number(input[0]);
const Cards = input[1].split(' ').map(Number); 

// M: 확인할 숫자 개수
const M = Number(input[2]);
const targets = input[3].split(' ').map(Number);

const cardCount = new Map();

// 카드 숫자를 순회하며 등장 횟수를 기록
Cards.forEach(num => {
  cardCount.set(num, (cardCount.get(num) || 0) + 1);
});

const result = [];

// 확인할 숫자들에 대해 Map에서 개수 조회
targets.forEach(num => {
  // 없으면 0, 있으면 개수 추가
  result.push(cardCount.get(num) || 0);
});

console.log(result.join(' '));