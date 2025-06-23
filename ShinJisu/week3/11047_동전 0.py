# 백준 11047_동전 0
# 주어진 가치의 동전들로 목표 금액을 만들 때 필요한 최소 동전 개수를 구하기 위해 가장 큰 동전부터 최대한 사용하는 그리디 알고리즘 적용 !

n, k = map(int, input().split())
coins = []

for _ in range(n):
   coins.append(int(input()))

# 큰 동전부터 확인하기 위해 리스트 뒤집기
coins.reverse()

count = 0
remaining = k

# 큰 동전부터 최대한 사용
for coin in coins:
   coin_count = remaining // coin
   count += coin_count
   remaining -= coin_count * coin
   
   if remaining == 0:
       break

print(count)