// const fs = require("fs");
// const input = fs
//   .readFileSync("run.txt")
//   .toString()
//   .trim()
//   .split("\n")
//   .map(Number);
// const n = input.shift();

// function quickSort(arr) {
//   if (arr.length <= 1) return arr;

//   const pivot = arr[Math.floor(arr.length / 2)];
//   const left = [],
//     right = [],
//     equal = [];

//   for (let num of arr) {
//     if (num < pivot) left.push(num);
//     else if (num > pivot) right.push(num);
//     else equal.push(num);
//   }

//   return [...quickSort(left), ...equal, ...quickSort(right)];
// }

// const sorted = quickSort(input);
// console.log(sorted.join("\n"));

const fs = require("fs");
const input = fs
  .readFileSync("run.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);
input.shift(); 

input.sort((a, b) => a - b);
console.log(input.join("\n"));
