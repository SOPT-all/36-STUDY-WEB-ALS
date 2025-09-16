# https://www.acmicpc.net/problem/2231

N = int(input())

def get_decomposition_sum(x):
    return x + sum(map(int, str(x)))

result = 0
for i in range(1, N):
    if get_decomposition_sum(i) == N:
        result = i
        break

print(result)