# https://www.acmicpc.net/problem/11279

import heapq

n = int(input()) # 명령의 개수 입력받기

h = []  # 최대 힙으로 사용할 리스트

for _ in range(n):
    x = int(input())   # 명령 하나 입력받기

    if x == 0:
        # 0이면 현재 힙에서 가장 큰 값을 꺼내 출력해야 함
        if len(h) == 0:
            print(0)  # 힙이 비어있으면 0 출력
        else:
            num = heapq.heappop(h)
            print(-num)  # 음수로 저장했으므로 다시 양수로 바꿔서 출력
    else:
        # x가 0이 아닌 경우에 힙에 추가
        heapq.heappush(h, -x)