# https://www.acmicpc.net/problem/1083

# 먼저 입력받을 수 의 개수를 입력받음
n = int(input())

# 수열을 공백으로 구분, 입력받고 정수형 리스트로 변환해줌 
arr = list(map(int, input().split()))

# 마지막으로 교환 횟수 S를 입력받음
S = int(input())

def bubble_sort(arr, S): # 배열 arr와 교환 횟수 S를 받는 함수
    n = len(arr)         # 배열의 길이를 n에 저장
    
    for i in range(n):   # i는 현재 위치고 왼쪽부터 차례대로 진행함
        if S == 0: 
            break        # 교환 횟수를 다 쓰면 정렬 중단

         # 뒤쪽에서부터 앞(i)으로 오면서 큰 값을 앞쪽으로 끌어옴 
         # 예를 들어 i=1이면 j는 n-1부터 i+1까지 줄어들며 봄
        for j in range(n - 1, i, -1):  
            if S == 0:
                break   # 교환 횟수를 다 쓰면 정렬 중단
            
            if arr[j - 1] < arr[j]:   # 만약 뒤에 숫자가 더 크면
                arr[j - 1], arr[j] = arr[j], arr[j - 1] # 둘을 바꿈
                S -= 1  # 교환 하면 교환횟수 하나 줄임
                
    return arr          # 정렬된 배열 반환

# 버블정렬 함수 실행함
result = bubble_sort(arr, S)

# 수열을 한줄로 출력함 
for num in result:
    print(num, end=' ')