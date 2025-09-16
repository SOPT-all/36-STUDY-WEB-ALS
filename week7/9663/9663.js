const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString().trim());

const col = Array(N).fill(false);            // 각 열에 퀸 배치 여부
const diag1 = Array(2 * N).fill(false);      // \ 대각선 (row + col)
const diag2 = Array(2 * N).fill(false);      // / 대각선 (row - col + N - 1)

let result = 0;

function dfs(row) {
  if (row === N) {
    result++;
    return;
  }

  for (let c = 0; c < N; c++) {
    if (col[c] || diag1[row + c] || diag2[row - c + N - 1]) continue;
    col[c] = diag1[row + c] = diag2[row - c + N - 1] = true;
    dfs(row + 1);
    col[c] = diag1[row + c] = diag2[row - c + N - 1] = false;
  }
}

dfs(0);
console.log(result);
