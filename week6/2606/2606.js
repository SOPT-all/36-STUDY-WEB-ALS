const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// n은 컴퓨터 수, m은 연결 정보 수
const n = Number(input[0]);
const m = Number(input[1]);

// 인접 리스트 초기화 (1번 인덱스부터 사용)
const graph = Array.from({ length: n + 1 }, () => []);
const visited = Array(n + 1).fill(false);

// 연결된 컴퓨터 정보 저장 (양방향 그래프)
for (let i = 2; i < 2 + m; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

let count = 0;

function dfs(v) {
  visited[v] = true;

  for (const next of graph[v]) {
    if (!visited[next]) {
      count++;
      dfs(next);
    }
  }
}

dfs(1);

console.log(count);
