# 백준 2606_바이러스
# 1번 컴퓨터에서 시작해서 네트워크로 연결된 모든 컴퓨터에 바이러스 전파
# 1번과 연결된 모든 컴퓨터 개수 구하기 (1번 제외)
# 1번에서 DFS로 탐색해서 방문한 컴퓨터 개수를 세고 1 빼기

N = int(input())
M = int(input())

# 그래프 만들기
graph = [[] for _ in range(N + 1)]

# 네트워크 연결 정보 입력
# a-b 연결이면 a에서 b로, b에서 a로 갈 수 있음
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS로 1번 컴퓨터와 연결된 모든 컴퓨터 찾기
def dfs(start):
    visited = [False] * (N + 1)
    count = 0
    
    def dfs_recursive(node):
        nonlocal count
        visited[node] = True
        count += 1
        
        # 현재 컴퓨터와 연결된 모든 컴퓨터 확인
        for next_node in graph[node]:
            if not visited[next_node]:  # 아직 감염 안됐으면
                dfs_recursive(next_node)  # 그 컴퓨터로 바이러스 전파
    
    dfs_recursive(start)
    return count - 1  # 1번 컴퓨터 제외

print(dfs(1))