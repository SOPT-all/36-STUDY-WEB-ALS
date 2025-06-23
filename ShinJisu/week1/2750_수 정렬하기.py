# 백준 2750_수 정렬하기
# 파이썬의 내장 정렬 함수 sort()를 사용하여 간단하게 해결 !

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

# 방법 1: sort() 메서드 사용
# 오름차순 정렬 - 원본 리스트를 직접 변경함 (제자리 정렬)
numbers.sort()

# 방법 2: sorted() 함수 사용
# 원본 리스트는 유지하고, 정렬된 새로운 리스트를 반환함
# sorted_numbers = sorted(numbers)  

# sort()를 사용했으므로 numbers가 이미 정렬되어 있음
for num in numbers:
    print(num)