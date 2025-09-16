# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())  

visited = [False] * (n + 1)  
g = []  

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, g)))
        return
    
    for i in range(1, n + 1):
        if not visited[i]:  
            visited[i] = True  
            g.append(i)      
            dfs(depth + 1)     
            visited[i] = False
            g.pop()

dfs(0)  