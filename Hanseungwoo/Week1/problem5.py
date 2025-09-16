# https://www.acmicpc.net/problem/1015

n = int(input())  # 수열 길이 입력받음

A = list(map(int, input().split()))  # 수열을 공백으로 구분, 입력받고 정수형 리스트로 변환해줌 

nums = []  # 빈 리스트를 만듬      

# 수열의 각 값을 값과 인덱스 형태로 저장함함
for i in range(n):
    nums.append((A[i], i)) 

# 값 기준으로 오름차순 정렬
nums.sort()

P = [0] * n  # 결과를 저장할 리스트 P 생성, 모두 0으로 초기화
