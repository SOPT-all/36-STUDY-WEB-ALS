# 백준 2751_수 정렬하기 2
# 병합 정렬을 활용한 정렬 문제 해결
# 이 문제는 최대 1,000,000개의 수를 정렬해야 하므로 O(N²) 알고리즘으로는 시간 초과가 발생함
# 병합 정렬은 분할 정복 전략을 사용하여 배열을 계속 반으로 나누고, 작은 부분부터 정렬하며 병합하는 방식
# 안정 정렬이며 최선/평균/최악 경우 모두 O(N log N)의 시간복잡도를 보장하여 대용량 데이터 처리에 적합함

import sys

n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # 두 배열의 원소를 비교하여 작은 것부터 result에 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 남은 원소들 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 병합 정렬 실행
sorted_numbers = merge_sort(numbers)

for num in sorted_numbers:
    print(num)