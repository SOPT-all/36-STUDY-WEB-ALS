# 백준 1541_잃어버린 괄호
# 마이너스 기호를 기준으로 나누고 첫 부분은 더하고 나머지는 빼기

expr = input().strip()

parts = expr.split('-')

# 첫 부분의 모든 수 더하기
res = sum(map(int, parts[0].split('+')))

# 나머지 부분들은 다 빼기
for part in parts[1:]:
   res -= sum(map(int, part.split('+')))

print(res)