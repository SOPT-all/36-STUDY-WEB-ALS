# 백준 2309_일곱 난쟁이
# 9명 중 2명을 제외해서 나머지 7명의 키 합이 100이 되는 경우를 찾는 문제
# 전체 합에서 100을 빼면 제외해야 할 2명의 키 합을 구할 수 있음 !!

heights = []
for _ in range(9):
   heights.append(int(input()))

total = sum(heights)
target = total - 100  # 제외해야 할 2명의 키 합

# 9명 중 2명을 선택하는 모든 경우 확인 -> 브루트포스
found = False
for i in range(9):
   if found:
       break
   for j in range(i + 1, 9):
       if heights[i] + heights[j] == target:
           # 이 2명을 제외하고 나머지 7명 출력
           result = []
           for k in range(9):
               if k != i and k != j:
                   result.append(heights[k])
           
           result.sort()
           for height in result:
               print(height)
           found = True
           break