# https://www.acmicpc.net/problem/2750

# 정수 입력 받음
n = int(input())

# 입력한 숫자를 저장할 빈 리스트를 만듬
nums = []

# n번 반복하면서 한 줄씩 숫자를 입력받고 리스트에 추가함 
for _ in range(n):
    nums.append(int(input()))

# 리스트에 저장된 숫자들을 오름차순으로 정렬해줌 
nums.sort()

# 정렬된 숫자들을 하나씩 출력함
for num in nums:
    print(num)