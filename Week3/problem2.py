# https://www.acmicpc.net/problem/11047

# 동전 종류랑 금액 합 설정함
n, k = map(int, input().split())

coins = []

# 각 종류의 금액을 입력 받아서 리스트에 저장함
for _ in range(n):
    coins.append(int(input()))

# 가장 큰 금액부터 탐색하기 위해서 리스트 뒤집는다.
coins.reverse()  

# 필요한 동전 개수 설정
count = 0  

for coin in coins:
    if k >= coin:
        count += k // coin    
        k = k % coin           

print(count)