# 백준 1764_듣보잡
# 듣도 못한 사람과 보도 못한 사람 중에서 겹치는 사람을 찾는 문제 !
# 듣도 못한 사람들을 set에 저장하고, 보도 못한 사람을 하나씩 확인하며 set에 있는지 확인

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 듣도 못한 사람들을 set에 저장
not_heard = set()
for _ in range(n):
   not_heard.add(input().strip())

# 보도 못한 사람 중에서 듣도 못한 사람과 겹치는 사람 찾기
res = []
for _ in range(m):
   name = input().strip()
   if name in not_heard:  # 교집합 확인
       res.append(name)

res.sort()

print(len(res))
for name in res:
   print(name)