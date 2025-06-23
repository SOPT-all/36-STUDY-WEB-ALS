# 백준 2667_단지번호붙이기
# 연결된 집들의 덩어리 개수와 각 덩어리의 크기 구하기
# DFS로 한 덩어리씩 찾아서 크기 계산하고 오름차순 정렬

import sys
input = sys.stdin.readline

def dfs(graph, visited, y, x, N):
    visited[y][x] = True
    cnt = 1  # 현재 집 포함
    
    # 상하좌우 이동
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    # 상하좌우 4방향 확인
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < N and 0 <= nx < N:
            if graph[ny][nx] == '1' and not visited[ny][nx]:
                cnt += dfs(graph, visited, ny, nx, N)
    
    return cnt

N = int(input())

# 지도 입력받기
graph = []
for _ in range(N):
    graph.append(input().strip())

visited = [[False] * N for _ in range(N)]
res = []  # 각 단지의 집 개수 저장

# 모든 위치 확인
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not visited[i][j]:
            house_cnt = dfs(graph, visited, i, j, N)
            res.append(house_cnt)


print(len(res))

res.sort()
for cnt in res:
    print(cnt)