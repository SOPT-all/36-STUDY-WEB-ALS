const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = parseInt(input[0]);
let line = 1;

for (let t = 0; t < T; t++) {
  // M: 가로 길이, N: 세로 길이, K: 배추 개수
  const [M, N, K] = input[line++].split(' ').map(Number);

  // 2차원 배추밭 배열 초기화
  const field = Array.from({ length: N }, () => Array(M).fill(0));

  // 배추 위치 입력받아 표시 (1)
  for (let i = 0; i < K; i++) {
    const [x, y] = input[line++].split(' ').map(Number);
    field[y][x] = 1;
  }

  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];

  // DFS 함수: 현재 위치에서 연결된 모든 배추 방문 처리
  const dfs = (x, y) => {
    field[y][x] = 0;

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      // 다음 위치가 유효 범위 내이고, 배추가 있는 곳이면 재귀 호출
      if (nx >= 0 && nx < M && ny >= 0 && ny < N && field[ny][nx] === 1) {
        dfs(nx, ny);
      }
    }
  };

  let count = 0;

  // 밭 전체를 탐색하면서 배추(1)를 찾으면 DFS 수행
  for (let y = 0; y < N; y++) {
    for (let x = 0; x < M; x++) {
      if (field[y][x] === 1) {
        dfs(x, y);
        count++;
      }
    }
  }

  console.log(count);
}
