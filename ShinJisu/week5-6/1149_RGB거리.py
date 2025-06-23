# 백준 1149_RGB거리
# 인접한 집은 같은 색깔로 칠할 수 없음
# 각 집을 R, G, B로 칠하는 최소 비용 구하기
# DP: 이전 집의 색깔에 따라 현재 집에서 선택 가능한 색깔이 달라짐 !

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
dp[0] = arr[0]  # 첫 행은 비용 그대로

for i in range(1, n):
    # 현재 열을 제외한 i-1행의 열들 중 최솟값 + 현재 칸 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n-1]))