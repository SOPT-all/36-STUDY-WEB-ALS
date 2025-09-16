# https://www.acmicpc.net/problem/10816

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

m = int(input())
tgs = list(map(int, input().split()))

counter = Counter(card)

result = [str(counter[tg]) for tg in tgs]
print(' '.join(result))
