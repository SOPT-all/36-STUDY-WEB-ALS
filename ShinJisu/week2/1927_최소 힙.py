# 백준 1927_최소 힙
# 최소 힙: 부모 노드의 값이 자식 노드의 값보다 항상 작거나 같은 완전 이진 트리
# 파이썬의 heapq는 기본적으로 최소 힙이므로 그대로 사용하면 됨
# 연산의 시간복잡도: 삽입/삭제 모두 O(log N)으로 총 시간복잡도는 O(N log N)

import sys
import heapq

n = int(sys.stdin.readline())
heap = []  # 최소 힙으로 사용할 리스트

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:  # 최솟값 출력 및 제거 연산
        if not heap:
            print(0)
        else:
            # heappop()은 힙에서 가장 작은 값(루트 노드)을 제거하고 반환
            print(heapq.heappop(heap))
    else:  # x가 자연수라면 배열에 x값을 추가하는 연산
        # 최소 힙은 그대로 값을 넣으면 됨
        heapq.heappush(heap, x)