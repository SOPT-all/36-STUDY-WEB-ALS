# https://www.acmicpc.net/problem/1931

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 정렬 기준 함수 정의 (끝나는ㄴ 시간이랑 그다음 시작 시간을 기준으로 둠)
def sort_by_end_then_start(meeting):
    return (meeting[1], meeting[0])

# 정렬 시킴 
meetings.sort(key=sort_by_end_then_start)

# 회의 선택
count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)