const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0]);
const lectures = input.slice(1).map(line => line.split(" ").map(Number));

// 시작 시간 기준 정렬 (같은 시간일 땐 끝나는 시간 순)
lectures.sort((a, b) => { 
  if (a[0] !== b[0]) return a[0] - b[0];
  return a[1] - b[1];
});

// 최소 힙 (종료 시간 기준)
class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(val) {
    this.heap.push(val); 
    let i = this.heap.length - 1;
    while (i > 0) {
      const parent = Math.floor((i - 1) / 2); 
      if (this.heap[parent] <= this.heap[i]) break;
      [this.heap[i], this.heap[parent]] = [this.heap[parent], this.heap[i]];
      i = parent;
    }
  }

  pop() {
    if (this.heap.length === 1) return this.heap.pop();
    const top = this.heap[0];
    this.heap[0] = this.heap.pop();

    let i = 0;
    while (true) {
      const left = i * 2 + 1;
      const right = i * 2 + 2;
      let smallest = i;

      if (left < this.heap.length && this.heap[left] < this.heap[smallest]) smallest = left;
      if (right < this.heap.length && this.heap[right] < this.heap[smallest]) smallest = right;
      if (smallest === i) break;

      [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
      i = smallest;
    }

    return top;
  }

  peek() {
    return this.heap[0];
  }

  size() {
    return this.heap.length;
  }
}

const heap = new MinHeap();

// 첫 강의 종료 시간 추가
heap.push(lectures[0][1]);

for (let i = 1; i < N; i++) {
  const [start, end] = lectures[i];

  // 가장 빨리 끝나는 강의실이 비었으면 그 강의실 재사용
  if (start >= heap.peek()) {
    heap.pop();
  }

  heap.push(end); // 새 강의실 사용 또는 기존 갱신
}

console.log(heap.size()); // 필요한 최소 강의실 수
