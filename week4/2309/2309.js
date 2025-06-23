const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const result = [];

for (let i = 0; i < 9; i++) {
  for (let j = i + 1; j < 9; j++) {

    // filter를 사용해서 인덱스 i, j를 제외한 원소들만 남김
    const temp = input.filter((_, idx) => idx !== i && idx !== j);

    // 선택된 7명의 키의 합 계산
    const sum = temp.reduce((a, b) => a + b, 0);

    // 만약 합이 100이면, 정답 조합 찾음
    if (sum === 100) {
      result.push(...temp); // temp 배열의 값들을 result에 push
      break;
    }
  }

  if (result.length > 0) break;
}

result.sort((a, b) => a - b);

result.forEach(v => console.log(v));
