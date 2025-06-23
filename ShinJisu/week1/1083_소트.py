# 백준 1083_소트
# 사전순으로 가장 큰 배열을 만들려면 배열에서 큰 값이 앞쪽에 위치해야 함
# 각 값을 최대한 앞으로 이동시켜야 하지만, 교환 횟수 제한을 고려해야 함
# 인접한 원소만 교환할 수 있으므로, 원소를 n칸 앞으로 이동시키려면 n번의 교환이 필요함
# 주어진 횟수를 가장 효과적으로 사용하려면 큰 값부터 최대한 앞으로 이동시켜야 함

n = int(input())
nums = list(map(int, input().split()))
swap_limit = int(input())

def find_largest_order(nums, swap_limit):
    n = len(nums)
    result = nums.copy()
    swaps_left = swap_limit

    pos = 0
    while pos < n and swaps_left > 0:
        # 현재 위치부터 교환 가능한 범위 내에서 최대값 찾기
        max_idx = pos
        # 현재 위치에서 남은 교환 횟수만큼 확인
        max_range = min(n-1, pos + swaps_left)
        
        for i in range(pos, max_range + 1):
            if result[i] > result[max_idx]:
                max_idx = i
        
        # 최대값을 현재 위치로 이동 (버블 정렬 방식)
        for i in range(max_idx, pos, -1):
            result[i], result[i-1] = result[i-1], result[i]
            swaps_left -= 1
        
        pos += 1
    
    return result

result = find_largest_order(nums, swap_limit)
print(" ".join(map(str, result)))