const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = +input[0]; // 마을 수
const population = [0, ...input[1].split(' ').map(Number)]; // 주민 수 (1-indexed)
const graph = Array.from({ length: N + 1 }, () => []);
const visited = Array(N + 1).fill(false);
const dp = Array.from({ length: N + 1 }, () => [0, 0]);

for (let i = 2; i < input.length; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

function dfs(node) {
  visited[node] = true;

  dp[node][0] = 0;                 // 이 노드를 우수 마을로 선택하지 않은 경우
  dp[node][1] = population[node]; // 이 노드를 우수 마을로 선택한 경우

  for (const next of graph[node]) {
    if (!visited[next]) {
      dfs(next);

      // 현재 노드를 선택하지 않은 경우: 자식 노드 선택 여부는 자유
      dp[node][0] += Math.max(dp[next][0], dp[next][1]);

      // 현재 노드를 선택한 경우: 자식 노드는 선택하면 안 됨
      dp[node][1] += dp[next][0];
    }
  }
}

dfs(1); // 루트를 1번 마을로 가정하고 시작

console.log(Math.max(dp[1][0], dp[1][1])); // 최대값 출력
