# https://www.acmicpc.net/problem/1427

# 문자열 형태로 숫자를 입력받음
n = input()

# 빈 리스트를 만듬      
nums = []         

# 입력받은 문자열에서 한 글자씩 정수형으로 변환해서 리스트에 추가함함
for num in n:
    nums.append(int(num))

# 노션참고 (선택 정렬 이용, 내림차순)
for i in range(len(nums)):
    max_idx = i                         # 현재 위치 = 최댓값의 위치
    for j in range(i + 1, len(nums)):   # i 뒤에 있는 모든 숫자와 비교
        if nums[j] > nums[max_idx]:     # 더 큰 수 찾으면
            max_idx = j                 # 최댓값 전환 
    nums[i], nums[max_idx] = nums[max_idx], nums[i] # 최댓값과 i번째 값 자리 변경 

# 정렬 시킨 숫자를 한 줄로 출력 시킴
for fin in nums:
    print(fin, end='')