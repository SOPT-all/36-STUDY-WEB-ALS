# 백준 1012_유기농 배추
# 붙어있는 배추 덩어리 개수 구하기
# 한 덩어리당 지렁이 1마리 필요

import sys
input = sys.stdin.readline

# 재귀 깊이 늘리기 (배추밭 크기가 최대 50x50이라 충분히 커야 함)
sys.setrecursionlimit(10000)

def dfs(field, visited, y, x, N, M):
    visited[y][x] = True
    
    # 상하좌우 이동
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    # 상하좌우 4방향 확인
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < N and 0 <= nx < M:
            if field[ny][nx] == 1 and not visited[ny][nx]:
                dfs(field, visited, ny, nx, N, M)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    # 배추밭 만들기
    field = [[0] * M for _ in range(N)]
    
    # 배추 심기
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    # 모든 위치 확인
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(field, visited, i, j, N, M)
                cnt += 1
    
    print(cnt)