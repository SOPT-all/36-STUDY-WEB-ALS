# 백준 1931_회의실 배정
# 회의실을 최대한 많이 사용하기 위해 끝나는 시간이 빠른 회의부터 선택하는 그리디 알고리즘 사용

import sys

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같으면 시작 시간이 빠른 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start, end in meetings:
    # 현재 회의의 시작 시간이 마지막으로 선택된 회의의 종료 시간 이후라면 선택
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)