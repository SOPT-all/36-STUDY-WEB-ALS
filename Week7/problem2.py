# https://www.acmicpc.net/problem/9663

n = int(input())  
queen = [0] * n   
result = 0        

def is_valid(row):
    for i in range(row):
        if queen[i] == queen[row] or abs(row - i) == abs(queen[row] - queen[i]):
            return False
    return True

def dfs(row):
    global result
    if row == n:
        result += 1
        return
    for col in range(n):
        queen[row] = col  
        if is_valid(row): 
            dfs(row + 1)  

dfs(0)
print(result)
