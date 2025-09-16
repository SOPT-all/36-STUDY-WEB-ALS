# https://www.acmicpc.net/problem/2751

# 빠른 입력을 위해 sys 모듈 사용
import sys  

# 먼저 정렬할 숫자의 개수 입력받기
n = int(sys.stdin.readline()) 
 
# 빈 리스트 생성
nums = []  

# n번 반복하면서 정수 하나씩 리스트에 추가
for _ in range(n):
    num = int(sys.stdin.readline())   # 하나씩씩 정수 입력받음
    nums.append(num) # 입력받은 정수를 리스트에 추가

nums.sort()  # 리스트 오름차순 정렬

# 정렬된 숫자들 출력
for num in nums:
    print(num) 