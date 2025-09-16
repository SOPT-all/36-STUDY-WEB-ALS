# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10000)

T = int(input())  # 테스트 케이스

# 상하좌우 이동 방향 벡터
dx = [0, 0, -1, 1]  
dy = [-1, 1, 0, 0]  

def dfs(x, y):
    # 현재 위치 방문
    visited[y][x] = True  

    # 상하좌우 인접한 칸을 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 좌표가 범위를 벗어나지 않으면서, 배추가 있고, 아직 방문하지 않았다면 재귀 호출
        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

for _ in range(T):
    #가로, 세로, 배추 개수수
    M, N, K = map(int, input().split()) 
    # 배추밭 정보 
    graph = [[0] * M for _ in range(N)]  
    # 방문 여부
    visited = [[False] * M for _ in range(N)]   

    # 배추가 심어진 위치를 그래프에 표시
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    # 지렁이 수
    count = 0  

    # 모든 위치 순회, DFS
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                # 새로운 배추 그룹 발견 하면 카운트 증가함함
                count += 1  

    print(count)
