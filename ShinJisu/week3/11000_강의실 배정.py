# 백준 11000_강의실 배정
# 최소 강의실 개수를 구하는 문제
# 시작 시간 순으로 정렬 후 우선순위 큐인 힙을 사용해 현재 사용 중인 강의실 관리

import sys
import heapq

input = sys.stdin.readline

n = int(input())
lectures = []

for _ in range(n):
   start, end = map(int, input().split())
   lectures.append((start, end))

lectures.sort()

# 우선순위 큐로 종료 시간을 저장
rooms = []

# 첫 번째 강의의 종료 시간을 큐에 넣음
heapq.heappush(rooms, lectures[0][1])

for i in range(1, n):
   start, end = lectures[i]
   
   # 현재 강의 시작 시간이 가장 빨리 끝나는 강의실의 종료 시간보다 크거나 같으면
   # 해당 강의실 재사용 가능 -> 큐에서 꺼내고 새 종료 시간 넣기 !!
   if start >= rooms[0]:
       heapq.heappop(rooms)
   
   # 새 강의의 종료 시간을 큐에 추가
   heapq.heappush(rooms, end)

print(len(rooms))