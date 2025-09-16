# 백준 14888_연산자 끼워넣기  
# 주어진 연산자들을 모든 순서로 배치해보는 순열 문제 !!
# N-1개 위치에 연산자를 하나씩 배치하며 모든 경우의 수 탐색
# 왼쪽부터 순차 계산하며 최댓값과 최솟값을 갱신

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_res = -int(1e9)
min_res = int(1e9)

def backtrack(idx, cur, a, s, m, d):
    global max_res, min_res
    
    if idx == N:
        max_res = max(max_res, cur)
        min_res = min(min_res, cur)
        return
    
    # 덧셈
    if a > 0:
        backtrack(idx + 1, cur + nums[idx], a - 1, s, m, d)
    
    # 뺄셈  
    if s > 0:
        backtrack(idx + 1, cur - nums[idx], a, s - 1, m, d)
    
    # 곱셈
    if m > 0:
        backtrack(idx + 1, cur * nums[idx], a, s, m - 1, d)
    
    # 나눗셈
    if d > 0:
        backtrack(idx + 1, int(cur / nums[idx]), a, s, m, d - 1)

backtrack(1, nums[0], add, sub, mul, div)
print(max_res)
print(min_res)