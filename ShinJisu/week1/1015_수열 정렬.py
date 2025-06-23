# 백준 1015_수열 정렬
# 각 원소의 값과 원래 인덱스를 함께 저장 - 입력된 배열의 각 숫자가 어느 위치에 있었는지 기억
# 값 기준으로 정렬하여 비내림차순을 만들기 위한 순서 파악 - 저장한 쌍들을 '값'에 따라 작은 것부터 정렬
# 원래 인덱스와 정렬 후 인덱스 관계를 이용해 P 배열 구성

n = int(input())
arr = list(map(int, input().split()))

def find_sequence_P(n, arr):
    # 각 원소와 원래 인덱스를 함께 저장 [(값, 인덱스)]
    val_idx = [(arr[i], i) for i in range(n)]
    
    # 값 기준으로 오름차순 정렬 (같은 값이면 원래 인덱스 기준으로 정렬됨)
    val_idx.sort()
    
    result = [0] * n
    
    # 수열 P 구성
    for new_pos in range(n):
        # 정렬된 배열에서 new_pos 위치에 있는 값이 원래 배열의 어느 위치에 있었는지 알아내기
        orig_pos = val_idx[new_pos][1]
        # result[i] = j는 원래 i 위치의 값이 정렬 후 j 위치에 온다는 의미
        result[orig_pos] = new_pos
    
    return result

p_sequence = find_sequence_P(n, arr)

print(' '.join(map(str, p_sequence)))