# https://www.acmicpc.net/problem/2606

# 컴퓨터 수 
n = int(input())

# 연결된 쌍
m = int(input())

graph = [[] for _ in range(n + 1)]

# 연결 정보 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 기록
visited = [False] * (n + 1)

# dfs
def dfs(v):
    visited[v] = True
    # 자기 자신을 포함함함
    count = 1  
    for next_node in graph[v]:
        if not visited[next_node]:
            count += dfs(next_node)
    return count

# 자기를 제외한 첫번째부터 시작
print(dfs(1) - 1)