const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);

const map = input.slice(1).map(line => line.split('').map(Number));

const visited = Array.from({ length: N }, () => Array(N).fill(false));

const result = [];

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function dfs(x, y) {
  visited[x][y] = true;
  let count = 1;

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    // 범위 안에 있고 방문하지 않았으며 집이 있는 경우
    if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
      if (!visited[nx][ny] && map[nx][ny] === 1) {
        count += dfs(nx, ny); // 연결된 집 수 누적
      }
    }
  }

  return count;
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    // 집이 있고 아직 방문하지 않은 경우
    if (map[i][j] === 1 && !visited[i][j]) {
      result.push(dfs(i, j)); // 단지 하나 완성, 집 수 저장
    }
  }
}


console.log(result.length);   
result.sort((a, b) => a - b);   
result.forEach(cnt => console.log(cnt));
