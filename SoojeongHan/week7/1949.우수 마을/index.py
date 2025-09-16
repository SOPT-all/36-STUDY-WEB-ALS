import sys
# 재귀 깊이 제한 설정
sys.setrecursionlimit(10**6)

# 마을(노드)의 수 입력
N = int(sys.stdin.readline())

# 각 마을의 주민 수 (1번 마을부터 시작, 0 더미)
people = [0] + list(map(int, sys.stdin.readline().split()))

# 트리 구조를 인접 리스트로 저장
tree = [[] for _ in range(N+1)]

# dp[node][0]: node가 우수 마을이 아닐 때 최대 주민 수
# dp[node][1]: node가 우수 마을일 때 최대 주민 수
dp = [[0, 0] for _ in range(N+1)]

# DFS 탐색 시 방문 체크
visit = [False] * (N+1)

# 트리 간선 정보 입력
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS로 트리 순회하며 DP 계산
def dfs(node):
    visit[node] = True

    # 현재 마을을 우수 마을로 선택한 경우 주민 수 반영
    dp[node][1] += people[node]

    # 자식 노드 순회
    for child in tree[node]:
        if not visit[child]:
            dfs(child)

            # 현재 마을이 우수 마을이 아닐 경우: 자식 마을은 선택 or 비선택 모두 가능
            dp[node][0] += max(dp[child][0], dp[child][1])

            # 현재 마을이 우수 마을인 경우: 자식은 반드시 비우수 마을이어야 함
            dp[node][1] += dp[child][0]

# 1번 마을을 루트로 DFS 시작
dfs(1)

# 최댓값 출력 (1번 마을이 우수일 때 / 아닐 때 중 최대)
print(max(dp[1]))
