# https://www.acmicpc.net/problem/11000

# 우선순위 큐 사용
import heapq

# 강의 개수 입력
n = int(input())
lectures = []

# 강의의 시작과 종료시간을 입력하고 튜플로 저장함함
for _ in range(n):
    start, end = map(int, input().split())
    lectures.append((start, end))
# 시작 시간 기준 정렬
lectures.sort()

# 최소 힙을 생성, 현재 사용 중인 강의실들의 종료 시간만 저장
rooms = []
# 첫 번째 강의의 종료 시간을 제일 먼저 힙에 넣음
heapq.heappush(rooms, lectures[0][1])  

# 두 번째 강의부터 반복
for i in range(1, n):
    start, end = lectures[i]

    # 가장 빨리 끝나는 강의의 종료 시간 확인
    if rooms[0] <= start:
        
        # 현재 강의 시작 시간 >= 가장 빨리 끝나는 강의 종료 시간
        # 해당 방을 재사용 가능하므로 꺼냄 
        heapq.heappop(rooms)

    # 현재 강의의 종료 시간을 힙에 추가함함
    heapq.heappush(rooms, end)
    
print(len(rooms))