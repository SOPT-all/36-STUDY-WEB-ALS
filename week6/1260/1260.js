const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 첫 줄에서 정점(N), 간선(M), 시작 정점(V) 추출
const [N, M, V] = input[0].split(' ').map(Number);

const graph = Array.from({ length: N + 1 }, () => []);

// 간선 정보 입력을 바탕으로 인접 리스트 구성 (무방향)
for (let i = 1; i <= M; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

// 정점 번호가 작은 순서대로 방문하도록 각 리스트 오름차순 정렬
for (let i = 1; i <= N; i++) {
  graph[i].sort((a, b) => a - b);
}

// DFS 구현: 재귀 방식
const dfsResult = [];
const visitedDFS = Array(N + 1).fill(false);
function dfs(v) {
  visitedDFS[v] = true;       
  dfsResult.push(v);          
  for (const next of graph[v]) {
    if (!visitedDFS[next]) {  
      dfs(next);
    }
  }
}

// BFS 구현: 큐를 이용한 반복 방식
const bfsResult = [];
const visitedBFS = Array(N + 1).fill(false);
function bfs(start) {
  const queue = [start];       
  visitedBFS[start] = true;     
  while (queue.length) {
    const v = queue.shift();   
    bfsResult.push(v);          
    for (const next of graph[v]) {
      if (!visitedBFS[next]) {
        visitedBFS[next] = true;
        queue.push(next);     
      }
    }
  }
}

dfs(V);
bfs(V);

console.log(dfsResult.join(' '));
console.log(bfsResult.join(' '));
