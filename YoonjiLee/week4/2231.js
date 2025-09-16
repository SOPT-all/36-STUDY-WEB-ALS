const fs = require("fs");
const input = Number(fs.readFileSync("run.txt").toString().trim());

function getDigitSum(n) {
  return (
    n +
    n
      .toString()
      .split("")
      .reduce((acc, digit) => acc + Number(digit), 0)
  );
}

function findConstructor(n) {
  for (let i = 1; i <= n; i++) {
    if (getDigitSum(i) === n) {
      return i;
    }
  }
  return 0;
}

console.log(findConstructor(input));
