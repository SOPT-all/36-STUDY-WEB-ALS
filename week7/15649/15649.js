const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
const N = Number(input[0]); 
const M = Number(input[1]); 

const visited = Array(N + 1).fill(false); 
const arr = []; 

function dfs(depth) {
  // M개의 수를 선택한 경우 출력
  if (depth === M) {
    console.log(arr.join(' '));
    return;
  }

  // 1부터 N까지의 수를 순회하며 선택
  for (let i = 1; i <= N; i++) {
    if (!visited[i]) { 
      visited[i] = true; 
      arr.push(i);       
      dfs(depth + 1);    
      visited[i] = false; 
      arr.pop();        
    }
  }
}

dfs(0); 
