# 백준 10816_숫자 카드 2
# 해시를 이용한 빈도수 카운팅 -> 각 숫자의 개수를 딕셔너리에 저장 후 O(1)로 조회

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

# 딕셔너리으로 각 숫자의 개수 저장
card_cnt = {}

# 상근이가 가진 카드들의 개수 세기
for card in cards:
   card_cnt[card] = card_cnt.get(card, 0) + 1

# 질의에 대한 답 구하기
result = []
for query in queries:
   result.append(card_cnt.get(query, 0))

print(' '.join(map(str, result)))