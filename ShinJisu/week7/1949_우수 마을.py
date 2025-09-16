# 백준 1949_우수 마을
# 트리 DP 문제: 인접한 노드를 동시에 선택할 수 없는 조건에서 최대 가중치 합 구하기
# 각 노드에서 '우수마을로 선택' vs '선택하지 않음' 두 가지 상태로 나누어 DP 설계

import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def village(start):
    visited[start] = True
    
    # 자식 노드들을 모두 탐색하며 DP 값 계산
    for i in tree[start]:
        if not visited[i]:
            village(i)  # 자식 노드 먼저 계산
            
            # 현재 노드를 우수마을로 선택하지 않는 경우
            # -> 자식은 우수마을이어도 되고 아니어도 됨 (둘 중 최댓값 선택)
            dp[start][0] += max(dp[i][0], dp[i][1])
            
            # 현재 노드를 우수마을로 선택하는 경우  
            # -> 자식은 절대 우수마을이 될 수 없음 (인접 조건)
            dp[start][1] += dp[i][0]

n = int(input())
people = [0] + list(map(int, input().split()))  # 1번부터 시작

# 트리 구조를 인접리스트로 저장
tree = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]

# DP 배열 초기화
# dp[i][0]: i번 마을이 우수마을이 아닌 경우의 최대 인구수
# dp[i][1]: i번 마을이 우수마을인 경우의 최대 인구수 (초기값: 해당 마을 인구수)
dp = [[0, people[i]] for i in range(n+1)]

# 트리 간선 정보 입력 (양방향)
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 1번 노드를 루트로 하여 트리 DP 수행
village(1)

# 루트 노드(1번)에서 우수마을 선택/비선택 중 최댓값이 정답
# 어떤 노드를 루트로 잡아도 트리의 전체 최적해는 동일함
print(max(dp[1][0], dp[1][1]))