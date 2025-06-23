# 백준 11279_최대 힙
# 최대 힙: 부모 노드의 값이 자식 노드의 값보다 항상 크거나 같은 완전 이진 트리
# 파이썬의 heapq는 기본적으로 최소 힙이므로, 값의 부호를 바꿔서 최대 힙처럼 동작하게 함
# 연산의 시간복잡도: 삽입/삭제 모두 O(log N)으로 총 시간복잡도는 O(N log N)

import sys
import heapq

n = int(sys.stdin.readline())
heap = []  # 최대 힙으로 사용할 리스트

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:  # 최댓값 출력 및 제거 연산
        if not heap:  # 힙이 비어있는 경우
            print(0)
        else:
            # 최대 힙을 위해 음수로 저장했으므로 다시 양수로 변환하여 출력
            # heappop()은 힙에서 가장 작은 값(루트 노드)을 제거하고 반환
            print(-heapq.heappop(heap))
    # x가 자연수라면 배열에 x값을 추가하는 연산
    else:
        # 최대 힙을 구현하기 위해 부호를 바꿔서 저장
        heapq.heappush(heap, -x)