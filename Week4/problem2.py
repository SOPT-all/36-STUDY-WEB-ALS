# https://www.acmicpc.net/problem/1764

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 집합 저장
listen = set(input().strip() for _ in range(n))
see = set(input().strip() for _ in range(m))

# 교집합ㅂ
result = sorted(listen & see)

print(len(result))
for name in result:
    print(name)
    