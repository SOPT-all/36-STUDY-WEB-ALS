const fs = require('fs');
const [_, numsLine, opsLine] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const nums = numsLine.split(' ').map(Number);
const [addCnt, subCnt, mulCnt, divCnt] = opsLine.split(' ').map(Number);

let maxV = -Infinity, minV = Infinity;

function dfs(idx, current, add, sub, mul, div) {
  if (idx === nums.length) {
    maxV = Math.max(maxV, current);
    minV = Math.min(minV, current);
    return;
  }
  const nextNum = nums[idx];
  if (add > 0) dfs(idx + 1, current + nextNum, add - 1, sub, mul, div);
  if (sub > 0) dfs(idx + 1, current - nextNum, add, sub - 1, mul, div);
  if (mul > 0) dfs(idx + 1, current * nextNum, add, sub, mul - 1, div);
  if (div > 0) {
    const val = current < 0 ? -Math.trunc(-current / nextNum) : Math.trunc(current / nextNum);
    dfs(idx + 1, val, add, sub, mul, div - 1);
  }
}

dfs(1, nums[0], addCnt, subCnt, mulCnt, divCnt);
console.log(maxV);
console.log(minV);
