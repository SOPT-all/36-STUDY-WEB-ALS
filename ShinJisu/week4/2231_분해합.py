# 백준 2231_분해합
# 1부터 N까지 모든 수를 확인해서 분해합이 N과 같은 가장 작은 수 찾기
# 각 수의 분해합을 계산해서 N과 비교하는 브루트포스

n = int(input())

# 1부터 n까지 모든 수 확인
for i in range(1, n + 1):
   # i의 분해합 계산
   digit_sum = sum(int(digit) for digit in str(i))
   decomposition_sum = i + digit_sum
   
   # 분해합이 n과 같으면 i가 생성자 !!
   if decomposition_sum == n:
       print(i)
       break
else:
   # 생성자를 찾지 못한 경우
   print(0)