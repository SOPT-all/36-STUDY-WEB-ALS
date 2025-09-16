# https://www.acmicpc.net/problem/14888

from itertools import permutations

n = int(input())  
nums = list(map(int, input().split()))  
plus, minus, multiply, divide = map(int, input().split())  

max_val = -int(1e9)
min_val = int(1e9)

def dfs(p, m, mul, d, result, idx):
    global max_val, min_val
    if idx == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    if p:
        dfs(p - 1, m, mul, d, result + nums[idx], idx + 1)
    if m:
        dfs(p, m - 1, mul, d, result - nums[idx], idx + 1)
    if mul:
        dfs(p, m, mul - 1, d, result * nums[idx], idx + 1)
    if d:
        dfs(p, m, mul, d - 1, int(result / nums[idx]), idx + 1)

dfs(plus, minus, multiply, divide, nums[0], 1)
print(max_val)
print(min_val)