const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);

const cost = input.slice(1).map(line => line.split(' ').map(Number));

// dp[i][j] : i번째 집을 j색(0=R, 1=G, 2=B)으로 칠할 때 최소 비용
const dp = Array.from({ length: N }, () => Array(3).fill(0));

// 첫 번째 집은 주어진 비용 그대로
dp[0][0] = cost[0][0]; 
dp[0][1] = cost[0][1]; 
dp[0][2] = cost[0][2]; 

// 두 번째 집부터 계산
for (let i = 1; i < N; i++) {
  dp[i][0] = cost[i][0] + Math.min(dp[i - 1][1], dp[i - 1][2]); 
  dp[i][1] = cost[i][1] + Math.min(dp[i - 1][0], dp[i - 1][2]); 
  dp[i][2] = cost[i][2] + Math.min(dp[i - 1][0], dp[i - 1][1]); 
}

// 마지막 집까지 계산한 후, 최소 비용 출력
console.log(Math.min(...dp[N - 1]));
