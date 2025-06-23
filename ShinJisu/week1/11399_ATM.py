# 백준 11399_ATM
# 인출 시간이 짧은 사람이 먼저 ATM을 이용하면 전체 대기 시간이 최소화 !

n = int(input())
times = list(map(int, input().split()))

# 인출 시간이 짧은 순서대로 정렬
times.sort()

total_time = 0
waiting_time = 0

for time in times:
    waiting_time += time
    total_time += waiting_time

print(total_time)