# 백준 2839_설탕 배달
# 3kg와 5kg 봉지를 이용해 정확히 nkg을 만들 때 필요한 최소 봉지 수 구하기
# 가능한 5kg 봉지의 조합을 모두 확인하여 최적해 찾기

n = int(input())

res = -1

# 5kg 봉지를 0개부터 최대 개수까지 사용하는 모든 경우 확인
for five_cnt in range((n // 5) + 1):
   remaining = n - (five_cnt * 5)
   
   # 남은 무게가 3kg 봉지로 정확히 나누어 떨어지는 경우
   if remaining % 3 == 0:
       three_cnt = remaining // 3
       # 최소 봉지 개수 계산
       total_cnt = five_cnt + three_cnt
       
       # 처음 찾은 경우이거나 기존보다 더 적은 봉지를 사용하는 경우 결과 갱신
       if res == -1 or total_cnt < res:
           res = total_cnt

print(res)