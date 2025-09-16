const fs = require("fs");
const input = fs.readFileSync("run.txt").toString().trim();

const result = input
  .split("")
  .sort((a, b) => b - a)
  .join("");

console.log(result);
