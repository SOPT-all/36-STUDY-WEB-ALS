# https://www.acmicpc.net/problem/2839

# 설탕 무게 입력받기
n = int(input()) 

# 봉지 개수 
bag = 0  

while n >= 0:
    if n % 5 == 0:
        # 5kg으로 정확히 나눠떨어지면 5kg 봉지 개수에 추가
        bag += n // 5 
        print(bag)
        break
    n -= 3  # 5kg 안나눠지면 3kg로 써봄
    bag += 1  # 3kg 봉지 하나 쓴 거 기록함
else:
    # 정확하게 나누어 떨어지지 않으면 -1을 출력
    print(-1)