# https://www.acmicpc.net/problem/2667

from collections import deque

# 지도 크기
n = int(input())  
# 2차원 지도
graph = [list(map(int, input())) for _ in range(n)]  
# 방문 여부 기록
visited = [[False] * n for _ in range(n)]  

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1  # 시작 집

    while queue:
        x, y = queue.popleft()
        # 4가지 방향
        for i in range(4):  
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:  # 지도 범위 안
                if graph[nx][ny] == 1 and not visited[nx][ny]:  # 방문 안 한 곳
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
    return count

# 단지 수, 단지별 집 수 
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:  
            result.append(bfs(i, j))  


print(len(result)) 
for cnt in sorted(result):  
    print(cnt)
