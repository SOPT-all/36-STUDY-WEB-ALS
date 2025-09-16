# 백준 9663_N-Queen
# 각 행에 퀸을 하나씩 배치하면서 열, 대각선 충돌을 미리 체크
# visited 배열로 열과 대각선 사용 여부를 O(1)로 확인하여 최적화 !
# 대각선은 우하향(+), 좌하향(-) 두 방향으로 나누어 체크

N = int(input())
cnt = 0

# 최적화: 각 열과 대각선의 사용 여부를 미리 체크 !!
visited_col = [False] * N           # 열 체크
visited_diag1 = [False] * (2*N-1)   # 우하향 대각선 (row+col)
visited_diag2 = [False] * (2*N-1)   # 좌하향 대각선 (row-col+N-1)

def backtrack(row):
    global cnt
    
    if row == N:
        cnt += 1
        return
    
    for col in range(N):
        # O(1)로 충돌 체크 !!!
        if (not visited_col[col] and 
            not visited_diag1[row + col] and 
            not visited_diag2[row - col + N - 1]):
            
            # 퀸 배치
            visited_col[col] = True
            visited_diag1[row + col] = True
            visited_diag2[row - col + N - 1] = True
            
            backtrack(row + 1)
            
            # 백트래킹
            visited_col[col] = False
            visited_diag1[row + col] = False
            visited_diag2[row - col + N - 1] = False

backtrack(0)
print(cnt)