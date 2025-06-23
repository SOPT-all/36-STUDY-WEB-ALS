const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

// '-' 기준으로 나누기(뺄셈이 발생하는 지점)
const parts = input.split("-");  

// 각 파트를 '+' 기준으로 분리하고, 각 합을 구함
const sums = parts.map(part => { 
  return part.split("+").map(Number).reduce((acc, cur) => acc + cur, 0); 
});

// 첫 번째 값은 그대로 더하고, 나머지는 모두 빼줌
// (첫 번째 값은 sums[0]이고, 나머지 값들은 sums.slice(1)을 가져옴)
const result = sums.slice(1).reduce((acc, cur) => acc - cur, sums[0]); 

console.log(result);
