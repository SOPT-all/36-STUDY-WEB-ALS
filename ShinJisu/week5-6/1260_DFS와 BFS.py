# 백준 1260_DFS와 BFS
# 그래프를 DFS와 BFS 두 방식으로 탐색해서 결과 출력
# DFS -> 한 방향으로 끝까지 가고 막히면 되돌아와서 다른 길 탐색
# BFS -> 현재 위치에서 갈 수 있는 모든 곳을 먼저 방문하고 다음 단계로
# 작은 번호부터 방문해야 하므로 인접 리스트 정렬 필수

from collections import deque

N, M, V = map(int, input().split())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(N + 1)]

# 연결된 길 정보 받아서 그래프 만들기
# 1-2 연결이면 1에서 2로 갈수있고, 2에서 1로도 갈수있음
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # a번에서 b번으로
    graph[b].append(a)  # b번에서 a번으로

# 작은 번호부터 방문하기 위해 각 리스트를 오름차순 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS 구현 (재귀)
def dfs(start):
    visited = [False] * (N + 1)
    result = []
    
    def dfs_recursive(node):
        visited[node] = True
        result.append(node)
        
        # 현재 노드와 연결된 모든 노드 확인
        for next_node in graph[node]:
            if not visited[next_node]:  # 아직 방문 안했으면
                dfs_recursive(next_node)  # 그 노드로 이동해서 탐색
    
    dfs_recursive(start)
    return result

# BFS 구현 (큐)
def bfs(start):
    visited = [False] * (N + 1)
    res = []
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        node = queue.popleft()  # 큐에서 앞쪽 원소 제거
        res.append(node)
        
        # 현재 노드와 연결된 모든 노드 확인
        for next_node in graph[node]:
            if not visited[next_node]:  # 아직 방문 안했으면
                visited[next_node] = True  # 방문 체크하고
                queue.append(next_node)  # 대기열에 추가 !!
    
    return res

dfs_res = dfs(V)
bfs_res = bfs(V)

print(' '.join(map(str, dfs_res)))
print(' '.join(map(str, bfs_res)))