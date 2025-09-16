# https://www.acmicpc.net/problem/1260

from collections import deque

# 입력받고
n, m, v = map(int, input().split())

# 정점 번호가 1번부터 시작하므로 n+1
graph = [[] for _ in range(n + 1)]  

# 간선 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node, visited)

def bfs(v):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

# dfs 실행하자자
visited_dfs = [False] * (n + 1)
dfs(v, visited_dfs)
print()
# bfs 실행하자자
bfs(v)